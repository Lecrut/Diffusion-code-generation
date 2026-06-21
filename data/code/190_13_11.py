def check_element_presence(target, lst):
    return target in lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_value = 3
    print(check_element_presence(target_value, sample_list))