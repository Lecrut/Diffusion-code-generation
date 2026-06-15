import os
def create_dictionary_from_file(filepath):
    data = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    data[key] = value
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
if __name__ == '__main__':
    sample_filename = "sample_data.txt"
    with open(sample_filename, 'w') as f:
        f.write("apple:red\n")
        f.write("banana:yellow\n")
        f.write("grape:purple\n")
    print("--- Test Case 1: File Exists ---")
    dictionary1 = create_dictionary_from_file(sample_filename)
    if dictionary1 is not None:
        print(dictionary1)
    print("\n--- Test Case 2: File Does Not Exist ---")
    non_existent_filename = "missing_file.txt"
    dictionary2 = create_dictionary_from_file(non_existent_filename)
    if dictionary2 is None:
        print("Successfully handled FileNotFoundError for missing file.")
    import os
    os.remove(sample_filename)