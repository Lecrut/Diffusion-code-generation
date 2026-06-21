def filter_string(input_list, target):
    return [item for item in input_list if item != target]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'apple']
    filtered_list = filter_string(sample_list, 'apple')
    print(filtered_list)