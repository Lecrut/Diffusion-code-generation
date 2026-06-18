def check_list_equality(list1, list2):
    return list1 == list2
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = [3, 2, 1]
    list_d = [1, 2, 4]
    list_e = [1, 2]
    list_f = [1, 2, 3, 4]
    print(check_list_equality(list_a, list_b))
    print(check_list_equality(list_a, list_c))
    print(check_list_equality(list_a, list_d))
    print(check_list_equality(list_a, list_e))
    print(check_list_equality(list_f, list_a))