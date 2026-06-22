def check_equality(item1, item2):
    return item1 is item2 or (isinstance(item1, type(item2)) and item1 == item2)
if __name__ == '__main__':
    a = 5
    b = 5
    c = [1, 2, 3]
    d = [1, 2, 3]
    print(check_equality(a, b))
    print(check_equality(c, d))