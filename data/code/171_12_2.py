import csv
data = [
    ["Store Name", "Description"],
    ["Store A", "A large retail location"],
    ["Store B", "Small boutique shop"],
    ["Store C", "Warehouse and distribution center"]
]
file_path = "store_data.csv"
try:
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
except IOError as e:
    print(f"Error writing to file: {e}")
store_list = []
try:
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if len(row) == 2:
                store_name = row[0]
                description = row[1]
                store_list.append({
                    "Store Name": store_name,
                    "Description": description
                })
            else:
                print(f"Skipping malformed row: {row}")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An unexpected error occurred during file reading: {e}")
if __name__ == '__main__':
    print("Loaded Store Data:")
    for store in store_list:
        print(store)