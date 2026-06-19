def check_equality(item1, item2):
    return item1 is item2 or (isinstance(item1, type(item2)) and item1 == item2)
if __name__ == '__main__':
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    d = 'hello'
    e = 'hello'
    print(check_equality(a, b))
    print(check_equality(a, c))
    print(check_equality(d, e))