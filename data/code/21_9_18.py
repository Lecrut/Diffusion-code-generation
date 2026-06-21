def get_largest(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

if __name__ == '__main__':
    val_a = 5
    val_b = 12
    val_c = 8
    largest = get_largest(val_a, val_b, val_c)
    print(largest)
    largest2 = get_largest(100, 20, 30)
    print(largest2)
    largest3 = get_largest(-50, -100, -25)
    print(largest3)