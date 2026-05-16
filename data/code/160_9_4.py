def process_file(filename):
    item_dict = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                item_name = line.strip()
                if item_name:
                    item_dict[item_name] = True
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return item_dict
    return item_dict
if __name__ == '__main__':
    sample_filename = "items.txt"
    with open(sample_filename, 'w') as f:
        f.write("Apple\n")
        f.write("Banana\n")
        f.write("Cherry\n")
        f.write("Date\n")
    final_dictionary = process_file(sample_filename)
    print("Item Dictionary:")
    for item, value in final_dictionary.items():
        print(f"- {item}")