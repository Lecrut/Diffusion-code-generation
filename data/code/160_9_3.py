def process_items(filename):
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
        f.write("\n")
        f.write("Elderberry\n")
    final_dictionary = process_items(sample_filename)
    print("--- Item Dictionary ---")
    if final_dictionary:
        for item, value in final_dictionary.items():
            print(f"{item}: Present")
    else:
        print("The dictionary is empty.")