def store_strings_as_unique(string_list):
    result_dict = {}
    for s in string_list:
        result_dict[s] = s
    return result_dict
if __name__ == '__main__':
    sample_list = ["apple", "banana", "apple", "orange", "banana"]
    output = store_strings_as_unique(sample_list)
    print(output)