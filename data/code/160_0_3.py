def process_item_list(filename):
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
        f.write("Apple\n")
        f.write("Banana\n")
        f.write("Cherry\n")
        f.write("Date\n")
        f.write("\n")
    result_dictionary = process_item_list(sample_filename)
    print(result_dictionary)