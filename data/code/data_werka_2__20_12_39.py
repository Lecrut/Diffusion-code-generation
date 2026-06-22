def check_equality(item1, item2):
    are_identical = item1 is item2
    have_equal_value = item1 == item2
    return are_identical and have_equal_value
if __name__ == '__main__':
    list_a = [4, 5, 6]
    list_b = list_a
    list_c = [4, 5, 6]
    print(check_equality(list_a, list_b))
    print(check_equality(list_a, list_c))