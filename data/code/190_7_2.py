import os
def check_secret(filename, secret):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            items = content.split(',')
            for item in items:
                if item.strip() == secret:
                    return True
            return False
    except FileNotFoundError:
        return False
    except Exception:
        return False
if __name__ == '__main__':
    file_name = "data.txt"
    secret_string = "SECRET_KEY"
    with open(file_name, 'w') as f:
        f.write("item1,item2,SECRET_KEY,item4")
    result = check_secret(file_name, secret_string)
    if result:
        print(f"'{secret_string}' was found in the file.")
    else:
        print(f"'{secret_string}' was not found in the file.")