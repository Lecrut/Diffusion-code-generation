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
    expected_data = {
        'Apple': True,
        'Banana': True,
        'Cherry': True,
        'Date': True
    }
    assert loaded_data == expected_data
    os.remove(sample_filename)