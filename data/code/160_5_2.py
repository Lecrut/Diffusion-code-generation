def store_strings_immutably(string_list):
    result_dict = {}
    for s in string_list:
        result_dict[s] = tuple(s)
    return result_dict
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "apple"]
    immutable_dict = store_strings_immutably(sample_list)
    print(immutable_dict)
    print(type(immutable_dict["apple"]))