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
        "\n",
        "Date\n"
    ]
    file_name = "items.txt"
    with open(file_name, 'w') as f:
        f.writelines(sample_data)
    result_dict = read_items_to_dict(file_name)
    print(result_dict)