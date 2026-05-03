def check_equality(a, b):
    return a == b
if __name__ == '__main__':
    x = 10
    y = 10
    z = "hello"
    w = "hello"
    print(check_equality(x, y))
    print(check_equality(x, z))
    print(check_equality(w, w))