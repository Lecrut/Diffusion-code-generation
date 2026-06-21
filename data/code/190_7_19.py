def check_value_exists(iterable, target):
    return target in iterable

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_value = 3
    print(check_value_exists(sample_list, target_value))
    
    sample_set = {'apple', 'banana', 'cherry'}
    target_item = 'banana'
    print(check_value_exists(sample_set, target_item))