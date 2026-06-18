def process_item_list(filename):
    item_dict = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                item_name = line.strip()
                if item_name:
                    item_dict[item_name] = "placeholder"
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return item_dict
if __name__ == '__main__':
    sample_data = [
        "apple",
        "banana",
        "cherry",
        "date",
        ""
    ]
    filename = "items.txt"
    with open(filename, 'w') as f:
        for item in sample_data:
            f.write(item + "\n")
    result_dict = process_item_list(filename)
    print(result_dict)