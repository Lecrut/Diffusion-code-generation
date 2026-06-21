def read_items(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def print_first_and_last(items):
    if items:
        first_item = items[0]
        last_item = items[-1]
        print(f"First item: {first_item}")
        print(f"Last item: {last_item}")

if __name__ == '__main__':
    sample_filename = "sample_data.txt"
    with open(sample_filename, 'w') as f:
        f.write("Apple\nBanana\nCherry\n")

    items = read_items(sample_filename)
    print_first_and_last(items)