import csv
data = [
    {"store_name": "Store A", "description": "A large retail location"},
    {"store_name": "Store B", "description": "Small boutique shop"},
    {"store_name": "Store C", "description": "Warehouse and distribution center"}
]
def load_store_data(csv_data):
    store_list = []
    try:
        with open("store_data.csv", mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                store_list.append(row)
    except FileNotFoundError:
        print("Error: The file 'store_data.csv' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred during file reading: {e}")
        return None
    return store_list
if __name__ == '__main__':
    try:
        with open("store_data.csv", mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['store_name', 'description'])
            writer.writeheader()
            writer.writerows(data)
        loaded_data = load_store_data(data)
        if loaded_data is not None:
            print("Successfully loaded store data:")
            for store in loaded_data:
                print(f"Store Name: {store['store_name']}, Description: {store['description']}")
    except Exception as e:
        print(f"An error occurred during setup or execution: {e}")