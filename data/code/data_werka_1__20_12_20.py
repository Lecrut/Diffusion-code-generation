def check_equality(item1, item2):
    return item1 is item2 and item1 == item2
if __name__ == '__main__':
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    print(check_equality(a, b))
    print(check_equality(a, c))