def create_boolean_dict():
    data = {
        "is_active": True,
        "is_logged_in": False,
        "has_permission": True,
        "is_admin": False
    }
    return data
def check_key_value(data, key):
    if key in data:
        return data[key] is True
    return False
if __name__ == '__main__':
    my_dict = create_boolean_dict()
    print(f"The dictionary: {my_dict}")
    key1 = "is_active"
    result1 = check_key_value(my_dict, key1)
    print(f"Is the value for '{key1}' True? {result1}")
    key2 = "is_logged_in"
    result2 = check_key_value(my_dict, key2)
    print(f"Is the value for '{key2}' True? {result2}")
    key3 = "non_existent_key"
    result3 = check_key_value(my_dict, key3)
    print(f"Is the value for '{key3}' True? {result3}")