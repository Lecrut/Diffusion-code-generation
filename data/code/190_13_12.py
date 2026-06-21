def contains_element(lst, target):
    return target in lst

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_value = 30
    result = contains_element(sample_list, target_value)
    print(f"Does the list contain {target_value}? {result}")