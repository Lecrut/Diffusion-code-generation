def read_and_print_dict_from_file(filepath):
    try:
        with open(filepath, 'r') as file:
            data = {}
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(':')
                    if len(parts) == 2:
                        key = parts[0].strip()
                        value = parts[1].strip()
                        data[key] = value
            if data:
                print("--- Dictionary Content ---")
                for key, value in data.items():
                    print(f"{key}: {value}")
            else:
                print("File read successfully, but no key-value pairs found.")
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == '__main__':
    sample_data = {
        "name": "Alice",
        "age": "30",
        "city": "New York",
        "occupation": "Engineer"
    }
    file_content = (
        "name: Alice\n"
        "age: 30\n"
        "city: New York\n"
        "occupation: Engineer\n"
    )
    filename = "sample_data.txt"
    try:
        with open(filename, 'w') as f:
            f.write(file_content)
        read_and_print_dict_from_file(filename)
    except Exception as e:
        print(f"An error occurred during file operation: {e}")