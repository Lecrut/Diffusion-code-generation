def verify_equality(var1, var2):
    if type(var1) != type(var2):
        return False
    return var1 == var2
if __name__ == '__main__':
    a = 5
    b = 5
    c = '5'
    d = [1, 2, 3]
    e = [1, 2, 3]
    print(verify_equality(a, b))
    print(verify_equality(a, c))
    print(verify_equality(d, e))