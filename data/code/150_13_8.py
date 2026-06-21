def filter_string(string_list, target):
    return [s for s in string_list if s != target]

if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry', 'date']
    target_string = 'banana'
    result = filter_string(sample_data, target_string)
    print(result)