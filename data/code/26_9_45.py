is_first_element_greater = lambda l: l[0] > l[1] if len(l) >= 2 else False
if __name__ == '__main__':
    test_list = [9, 3]
    print(is_first_element_greater(test_list))