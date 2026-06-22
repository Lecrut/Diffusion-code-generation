def find_largest(a, b, c):
    return a if a >= b and a >= c else (b if b >= c else c)

if __name__ == '__main__':
    val_a = 10
    val_b = 25
    val_c = 18
    print(find_largest(val_a, val_b, val_c))