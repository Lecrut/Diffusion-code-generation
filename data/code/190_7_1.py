def check_secret(filename, secret):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            list_of_items = content.splitlines()
            if secret in list_of_items:
                print(f"Secret found in the list.")
            else:
                print(f"Secret not found in the list.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == '__main__':
    file_name = "data.txt"
    secret_string = "supersecret"
    with open(file_name, 'w') as f:
        f.write("apple\n")
        f.write("banana\n")
        f.write("supersecret\n")
        f.write("orange\n")
    check_secret(file_name, secret_string)