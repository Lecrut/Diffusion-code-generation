def find_largest(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

if __name__ == '__main__':
    val1 = 3.5
    val2 = 7.2
    val3 = 1.9
    result = find_largest(val1, val2, val3)
    print(result)