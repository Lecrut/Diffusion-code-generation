def read_and_check_list(filename):
    try:
        with open(filename, 'r') as file:
            items = file.readlines()
            if not items:
                print("File is empty.")
                return
            processed_items = [item.strip() for item in items]
            if not processed_items:
                print("File contains only empty lines.")
                return
            first_item = processed_items[0]
            last_item = processed_items[-1]
            print(f"First item: {first_item}")
            print(f"Last item: {last_item}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    sample_filename = "sample_data.txt"
    with open(sample_filename, 'w') as f:
        f.write("Apple\n")
        f.write("Banana\n")
        f.write("Cherry\n")
        f.write("Date\n")
    read_and_check_list(sample_filename)