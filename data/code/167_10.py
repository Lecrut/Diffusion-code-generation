def create_data_file(filename):
    with open(filename, 'w') as f:
        f.write("Store A,25\n")
        f.write("Store B,30\n")
        f.write("Store C,22\n")
        f.write("Store D,45\n")
def process_data(filename):
    data = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    store_name = parts[0].strip()
                    age = int(parts[1].strip())
                    data.append((store_name, age))
    except FileNotFoundError:
        return []
    return data
def print_table(data):
    if not data:
        print("No data to display.")
        return
    print("\n--- Store Information ---")
    max_store_len = max(len(name) for name, age in data) if data else 0
    header_name = "Store Name".ljust(max_store_len + 2)
    header_age = "Age".center(5)
    print(f"{header_name} | {header_age}")
    print("-" * (max_store_len + 10))
    for name, age in data:
        print(f"{name.ljust(max_store_len)} | {age}")
if __name__ == '__main__':
    FILE_NAME = "store_data.txt"
    create_data_file(FILE_NAME)
    store_data = process_data(FILE_NAME)
    print_table(store_data)