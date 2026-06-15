import csv
data = [
    {"store_name": "Store A", "description": "A large retail location"},
    {"store_name": "Store B", "description": "Small boutique shop"},
    {"store_name": "Store C", "description": "Warehouse and distribution center"}
]
def load_store_data(filename):
    store_list = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                store_list.append(row)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred during file reading: {e}")
        return None
    return store_list
if __name__ == '__main__':
    sample_filename = 'store_data.csv'
    with open(sample_filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["store_name", "description"])
        writer.writerow(["Store A", "A large retail location"])
        writer.writerow(["Store B", "Small boutique shop"])
        writer.writerow(["Store C", "Warehouse and distribution center"])
    loaded_data = load_store_data(sample_filename)
    if loaded_data is not None:
        print("Successfully loaded store data:")
        for store in loaded_data:
            print(f"Name: {store.get('store_name')}, Description: {store.get('description')}")
    else:
        print("Data loading failed.")