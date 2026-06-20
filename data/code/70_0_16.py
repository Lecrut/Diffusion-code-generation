def read_items_from_file(filename):
    try:
        with open(filename, 'r') as file:
            items = file.readlines()
            return items
    except FileNotFoundError:
        raise ValueError(f"Error: File '{filename}' not found.")
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")

def print_first_last(items):
    if not items:
        return
    first_item = items[0].strip()
    last_item = items[-1].strip()
    print(f"First item: {first_item}")
    print(f"Last item: {last_item}")

if __name__ == '__main__':
    sample_filename = "sample_data.txt"
    with open(sample_filename, 'w') as f:
        f.write("Apple\nBanana\nCherry\n")
    
    items = read_items_from_file(sample_filename)
    print_first_last(items)