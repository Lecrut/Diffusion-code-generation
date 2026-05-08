def create_and_check_dict():
    data = {
        "apple": True,
        "banana": False,
        "cherry": True,
        "date": False
    }
    def check_value(key):
        if key in data:
            return data[key]
        return None
    key_to_check = "apple"
    result = check_value(key_to_check)
    print(f"The value for '{key_to_check}' is True: {result is True}")
if __name__ == '__main__':
    create_and_check_dict()