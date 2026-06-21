def filter_string(input_list, string_to_remove):
    return [item for item in input_list if item != string_to_remove]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'banana']
    string_to_filter = 'banana'
    filtered_list = filter_string(sample_list, string_to_filter)
    print(filtered_list)