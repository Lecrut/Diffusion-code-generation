def verify_equality(var1, var2):
    return type(var1) == type(var2) and var1 == var2
if __name__ == '__main__':
    a = 42
    b = 42
    c = '42'
    d = [1, 2, 3]
    e = [1, 2, 3]
    print(verify_equality(a, b))
    print(verify_equality(a, c))
    print(verify_equality(d, e))