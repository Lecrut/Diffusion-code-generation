import csv
data = [
    {"store_name": "Store A", "description": "A large retail location"},
    {"store_name": "Store B", "description": "Small convenience shop"},
    {"store_name": "Store C", "description": "Electronics and gadgets"},
]
def read_and_load_data(filename):
    data_list = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_list.append(row)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during file reading: {e}")
        return None
    return data_list
if __name__ == '__main__':
    sample_filename = 'store_data.csv'
    try:
        with open(sample_filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["store_name", "description"])
            writer.writerow(["Store A", "A large retail location"])
            writer.writerow(["Store B", "Small convenience shop"])
            writer.writerow(["Store C", "Electronics and gadgets"])
        loaded_data = read_and_load_data(sample_filename)
        if loaded_data is not None:
            print("Successfully loaded data:")
            for item in loaded_data:
                print(item)
    except Exception as e:
        print(f"An error occurred during setup or execution: {e}")