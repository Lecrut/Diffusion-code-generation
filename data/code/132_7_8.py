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
    print("Dictionary created:")
    print(data)
    print("\nChecking values:")
    keys_to_check = ["apple", "banana", "cherry", "grape"]
    for key in keys_to_check:
        result = check_value_is_true(data, key)
        print(f"Is the value for '{key}' True? {result}")
if __name__ == '__main__':
    create_and_check_dictionary()