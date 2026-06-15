def check_secret(filename, secret):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            if secret in content:
                print(f"Secret found in the file.")
            else:
                print(f"Secret not found in the file.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == '__main__':
    file_name = "data.txt"
    secret_string = "supersecret123"
    with open(file_name, 'w') as f:
        f.write("this is a test line.\n")
        f.write("the secret is supersecret123.\n")
        f.write("another line.")
    check_secret(file_name, secret_string)