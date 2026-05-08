def create_and_check_dictionary():
    my_dict = {
        "apple": True,
        "banana": False,
        "cherry": True,
        "date": False
    }
    def check_key_value(data_dict, key):
        if key in data_dict:
            return data_dict[key]
        return None
    target_key = "apple"
    value = check_key_value(my_dict, target_key)
    if value is True:
        print(f"The value for '{target_key}' is True.")
    else:
        print(f"The value for '{target_key}' is not True.")
if __name__ == '__main__':
    create_and_check_dictionary()