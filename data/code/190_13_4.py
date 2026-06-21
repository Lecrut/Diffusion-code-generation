def contains_element(lst, target):
    return target in lst

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd', 'e']
    target_value1 = 'c'
    target_value2 = 'f'
    print(f"Does the list contain '{target_value1}'? {contains_element(sample_list, target_value1)}")
    print(f"Does the list contain '{target_value2}'? {contains_element(sample_list, target_value2)}")