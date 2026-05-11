def reverse_strings_to_dict(item_names):
    result_dict = {}
    for item in item_names:
        result_dict[item] = item[::-1]
    return result_dict
if __name__ == '__main__':
    sample_list = ["hello", "world", "python", "code"]
    reversed_dict = reverse_strings_to_dict(sample_list)
    print(reversed_dict)