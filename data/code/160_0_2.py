def read_items_to_dict(filename):
    item_dict = {}
    try:
        with open(filename, 'r') as file:
            item_names = file.readlines()
            for line in item_names:
                item_name = line.strip()
                if item_name:
                    item_dict[item_name] = True
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return item_dict
if __name__ == '__main__':
    sample_filename = "items.txt"
    with open(sample_filename, 'w') as f:
        f.write("apple\n")
        f.write("banana\n")
        f.write("cherry\n")
        f.write("date\n")
    result_dict = read_items_to_dict(sample_filename)
    print(result_dict)