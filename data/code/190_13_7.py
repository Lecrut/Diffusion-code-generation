def contains_element(lst, target):
    return target in lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_value1 = 3
    target_value2 = 6
    print(f"Does the list contain {target_value1}? {contains_element(sample_list, target_value1)}")
    print(f"Does the list contain {target_value2}? {contains_element(sample_list, target_value2)}")