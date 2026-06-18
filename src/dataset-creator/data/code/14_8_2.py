def store_unique_names(string_list):
    result_dict = {}
    for item in string_list:
        if item not in result_dict:
            result_dict[item] = item
    return result_dict
if __name__ == '__main__':
    sample_list = ["apple", "banana", "apple", "cherry", "banana", "date"]
    output = store_unique_names(sample_list)
    print(output)