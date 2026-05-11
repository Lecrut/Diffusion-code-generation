def read_items_to_dict(filename):
    item_dict = {}
    try:
        with open(filename, 'r') as file:
            item_names = file.readlines()
            for line in item_names:
                item = line.strip()
                if item:
                    item_dict[item] = True
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return item_dict
if __name__ == '__main__':
    sample_data = [
        "Apple\n",
        "Banana\n",
        "Cherry\n",
        "Date\n"
    ]
    filename = "items.txt"
    with open(filename, 'w') as f:
        f.writelines(sample_data)
    result_dict = read_items_to_dict(filename)
    print(result_dict)