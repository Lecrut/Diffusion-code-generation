def filter_string(lst, target):
    return [s for s in lst if s != target]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    target_string = 'banana'
    result = filter_string(sample_list, target_string)
    print(result)