def check_secret(filename, secret):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            items = content.splitlines()
            if secret in items:
                return True
            else:
                return False
    except FileNotFoundError:
        return False
    except Exception:
        return False
if __name__ == '__main__':
    file_name = "data.txt"
    secret_string = "SECRET_KEY_123"
    with open(file_name, 'w') as f:
        f.write("item1\n")
        f.write("SECRET_KEY_123\n")
        f.write("item3\n")
    result = check_secret(file_name, secret_string)
    if result:
        print(f"The secret string '{secret_string}' was found in the file.")
    else:
        print(f"The secret string '{secret_string}' was not found in the file.")