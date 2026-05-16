def read_and_print_first_and_last(filename):
    try:
        with open(filename, 'r') as file:
            items = file.readlines()
            if not items:
                return
            first_item = items[0].strip()
            last_item = items[-1].strip()
            print(f"First item: {first_item}")
            print(f"Last item: {last_item}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == '__main__':
    sample_filename = "sample_data.txt"
    with open(sample_filename, 'w') as f:
        f.write("Apple\n")
        f.write("Banana\n")
        f.write("Cherry\n")
        f.write("Date\n")
        f.write("Elderberry\n")
        f.write("Fig\n")
    read_and_print_first_and_last(sample_filename)