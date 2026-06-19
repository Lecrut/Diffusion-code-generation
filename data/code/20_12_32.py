def check_equality(item1, item2):
    return item1 is item2 and item1 == item2
if __name__ == '__main__':
    int_a = 42
    int_b = 42
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    print(check_equality(int_a, int_b))
    print(check_equality(list_a, list_b))