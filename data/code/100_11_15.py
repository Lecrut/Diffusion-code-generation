def check_all_elements(lst, condition):
    for element in lst:
        if not condition(element):
            return False
    return True
if __name__ == '__main__':
    sample_list = [True, True, True]
    print(check_all_elements(sample_list, lambda x: x))
    sample_list2 = [False, False, False]
    print(check_all_elements(sample_list2, lambda x: not x))
    sample_list3 = [True, False, True]
    print(check_all_elements(sample_list3, lambda x: x))