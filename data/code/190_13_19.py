def contains_element(lst, target):
    return target in lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_value = 3
    print(f"Does the list contain {target_value}? {contains_element(sample_list, target_value)}")