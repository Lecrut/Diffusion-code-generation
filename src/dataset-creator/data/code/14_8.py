def store_unique_strings(string_list):
    result_dict = {}
    for item in string_list:
        if item not in result_dict:
            result_dict[item] = item
    return result_dict
if __name__ == '__main__':
    sample_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
    output = store_unique_strings(sample_list)
    print(output)