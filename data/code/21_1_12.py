def get_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= c:
        return b
    return c

if __name__ == '__main__':
    val_a = 5
    val_b = 50
    val_c = 20
    maximum = get_maximum(val_a, val_b, val_c)
    print(maximum)