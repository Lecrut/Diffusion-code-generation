def create_and_check_dictionary():
    data = {
        "apple": True,
        "banana": False,
        "cherry": True,
        "date": False
    }
    def check_value_is_true(key):
        if key in data:
            return data[key] is True
        return False
    return data, check_value_is_true
if __name__ == '__main__':
    my_dict, check_key = create_and_check_dictionary()
    print("Dictionary:", my_dict)
    key_to_check = "apple"
    result = check_key(key_to_check)
    print(f"Is the value for '{key_to_check}' True? {result}")
    key_to_check = "banana"
    result = check_key(key_to_check)
    print(f"Is the value for '{key_to_check}' True? {result}")
    key_to_check = "grape"
    result = check_key(key_to_check)
    print(f"Is the value for '{key_to_check}' True? {result}")