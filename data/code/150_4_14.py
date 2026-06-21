def filter_string(lst, value):
    return [item for item in lst if item != value]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'apple']
    filtered_list = filter_string(sample_list, 'apple')
    print(filtered_list)