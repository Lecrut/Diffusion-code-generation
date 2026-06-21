def read_file_lines(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def validate_items(items):
    if not items:
        print("The file is empty.")
        return False
    return True

def print_first_and_last(items):
    first_item = items[0]
    last_item = items[-1]
    print(f"First item: {first_item}")
    print(f"Last item: {last_item}")

def read_and_print_first_last(filename):
    items = read_file_lines(filename)
    if validate_items(items):
        print_first_and_last(items)

if __name__ == '__main__':
    sample_filename = "sample_data.txt"
    with open(sample_filename, 'w') as f:
        f.write("Apple\nBanana\nCherry\n")
    read_and_print_first_last(sample_filename)