def check_equality(item1, item2):
    return item1 is item2 and item1 == item2
if __name__ == '__main__':
    LIST_A = [1, 2, 3]
    LIST_B = LIST_A
    LIST_C = [1, 2, 3]
    print(check_equality(LIST_A, LIST_B))
    print(check_equality(LIST_A, LIST_C))