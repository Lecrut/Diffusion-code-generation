import csv
data = [
    ["Store Name", "Description"],
    ["Store A", "A large retail location"],
    ["Store B", "Small boutique shop"],
    ["Store C", "Warehouse facility"]
]
file_path = "store_data.csv"
try:
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        store_list = []
        for row in reader:
            if len(row) == 2:
                store_list.append({header[0]: row[0], header[1]: row[1]})
            else:
                print(f"Skipping malformed row: {row}")
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found.")
    store_list = []
except Exception as e:
    print(f"An unexpected error occurred during file reading: {e}")
    store_list = []
if __name__ == '__main__':
    print("Loaded Store Data:")
    for store in store_list:
        print(store)