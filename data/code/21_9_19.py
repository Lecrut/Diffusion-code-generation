def find_largest(a, b, c):
    if a >= b:
        if a >= c:
            return a
        return c
    if b >= c:
        return b
    return c

if __name__ == '__main__':
    val_x = 45
    val_y = 92
    val_z = 18
    print(find_largest(val_x, val_y, val_z))
    print(find_largest(7, 7, 7))
    print(find_largest(-30, -12, -40))