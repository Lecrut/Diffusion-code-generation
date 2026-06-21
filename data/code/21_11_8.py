def get_largest(a, b, c):
    return a if a > b and a > c else (b if b > c else c)

if __name__ == '__main__':
    var1 = 10
    var2 = 25
    var3 = 15
    print(get_largest(var1, var2, var3))