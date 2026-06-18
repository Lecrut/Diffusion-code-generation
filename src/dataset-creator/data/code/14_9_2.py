import os
def load_item_names_from_file(filepath: str) -> dict:
    item_names = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                item_name = line.strip()
                if item_name:
                    item_names[item_name] = True
        return item_names
    except FileNotFoundError:
        return {}
    except Exception:
        return {}
if __name__ == '__main__':
    sample_filename = "sample_items.txt"
    with open(sample_filename, 'w') as f:
        f.write("Apple\n")
        f.write("Banana\n")
        f.write("Cherry\n")
        f.write("\n")
        f.write("Date\n")
    loaded_data = load_item_names_from_file(sample_filename)
    print(loaded_data)
    non_existent_file = "non_existent.txt"
    loaded_empty = load_item_names_from_file(non_existent_file)
    print(f"\nData from non-existent file: {loaded_empty}")
    os.remove(sample_filename)