import os
import json
import csv

def show_payment_methods():
    print("Wybierz metodę płatności: ")
    print("1. Karta               2. Paypal")

def wybor(opcja):
    os.system('cls')
    if opcja == '1':
        print("Wybrałeś metodę płatności: Karta")
        Karta()
        
    elif opcja == '2':
        print("Wybrałeś metodę płatności: Paypal")
        Paypal()
        
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")

def Karta():
    data = {}
    data['metoda'] = 'Karta'
    data['numer_karty'] = input("Podaj nr karty: ")
    data['data_waznosci'] = input("Podaj datę unieważnienia karty (MM/YY): ")
    data['ccv'] = input("Podaj nr CCV: ")
    potwierdzenie = input("Zatwierdź płatność, napisz 'tak': ")
    data['zatwierdzenie'] = potwierdzenie.strip().lower() == 'tak'
    save_to_json(data)

def Paypal():
    data = {}
    data['metoda'] = 'Paypal'
    data['email'] = input("Podaj adres email: ")
    data['haslo'] = input("Podaj hasło: ")
    potwierdzenie = input("Zatwierdź płatność, napisz 'tak': ")
    data['zatwierdzenie'] = potwierdzenie.strip().lower() == 'tak'
    save_to_json(data)

def save_to_json(data):
    try:
        with open('payment_data.json', 'r') as f:
            existing_data = json.load(f)
            if isinstance(existing_data, dict):  
                existing_data = [existing_data]
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []  

    existing_data.append(data)

    with open('payment_data.json', 'w') as f:
        json.dump(existing_data, f, indent=4)

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as jf:
        data = json.load(jf)
        

    fieldnames = set()
    for entry in data:
        fieldnames.update(entry.keys())


    with open(csv_file, 'w', newline='') as cf:
        writer = csv.DictWriter(cf, fieldnames=sorted(fieldnames))
        writer.writeheader()
        writer.writerows(data)

def main():
    show_payment_methods()
    opcja = input("Wybierz opcję (1 lub 2): ")
    wybor(opcja)
    json_to_csv('payment_data.json', 'payment_data.csv')
    print("Dane zostały zapisane do pliku payment_data.csv.")

if __name__ == "__main__":
    main()
