import os
def check_secret(filename, secret):
    try:
        with open(filename, 'r') as file:
            data = file.read().splitlines()
            return secret in data
    except FileNotFoundError:
        return False
    except Exception:
        return False
if __name__ == '__main__':
    file_name = "sample_list.txt"
    secret_string = "secret_phrase"
    with open(file_name, 'w') as f:
        f.write("apple\nbanana\ncherry\ndate")
    result = check_secret(file_name, secret_string)
    if result:
        print(f"The secret string '{secret_string}' was found in the list.")
    else:
        print(f"The secret string '{secret_string}' was not found in the list.")