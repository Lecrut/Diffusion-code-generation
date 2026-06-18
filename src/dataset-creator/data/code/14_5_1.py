def read_items_from_file(filepath):
    item_dict = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                item_name = line.strip()
                if item_name:
                    item_dict[item_name] = True
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    return item_dict
if __name__ == '__main__':
    sample_filename = "items.txt"
    with open(sample_filename, 'w') as f:
        f.write("apple\n")
        f.write("banana\n")
        f.write("cherry\n")
        f.write("\n")
        f.write("date\n")
    items = read_items_from_file(sample_filename)
    print(items)