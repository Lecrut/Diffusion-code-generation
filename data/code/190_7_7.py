def check_secret_in_file(filename, secret):
    try:
        with open(filename, 'r') as file:
            content = file.read().splitlines()
            return secret in content
    except FileNotFoundError:
        return False
    except Exception:
        return False
if __name__ == '__main__':
    file_name = "data.txt"
    secret_string = "secret_key_123"
    with open(file_name, 'w') as f:
        f.write("item_a\n")
        f.write("secret_key_123\n")
        f.write("item_b\n")
    result = check_secret_in_file(file_name, secret_string)
    if result:
        print(f"The secret string '{secret_string}' was found in the file.")
    else:
        print(f"The secret string '{secret_string}' was not found in the file.")