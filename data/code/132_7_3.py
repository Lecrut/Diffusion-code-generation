def create_and_check_dictionary():
    data = {
        "apple": True,
        "banana": False,
        "cherry": True,
        "date": False
    }
    def check_value_is_true(dictionary, key):
        if key in dictionary:
            return dictionary[key] is True
        return False
    key_to_check = "apple"
    result = check_value_is_true(data, key_to_check)
    print(f"The dictionary is: {data}")
    print(f"Checking if the value for '{key_to_check}' is True: {result}")
if __name__ == '__main__':
    create_and_check_dictionary()