def filter_string(input_list, value):
    return [item for item in input_list if item != value]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'banana', 'date']
    filtered_list = filter_string(sample_list, 'banana')
    print(filtered_list)