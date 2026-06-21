def filter_string(input_list, value_to_remove):
    return [item for item in input_list if item != value_to_remove]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'banana']
    value_to_remove = 'banana'
    print(filter_string(sample_list, value_to_remove))