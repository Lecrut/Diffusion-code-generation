def store_strings_immutably(string_list):
    result_dict = {}
    for index, s in enumerate(string_list):
        result_dict[f"item_{index}"] = (s,)
    return result_dict
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    immutable_dict = store_strings_immutably(sample_list)
    print(immutable_dict)
    print(type(immutable_dict["item_0"]))
    print(type(immutable_dict["item_1"]))