def find_middle_element(lst):
    return lst[len(lst) // 2]

if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    middle_value = find_middle_element(test_list)
    print(middle_value)