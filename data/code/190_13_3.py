def is_element_present(lst, target):
    return target in lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_value = 3
    print(is_element_present(sample_list, target_value))