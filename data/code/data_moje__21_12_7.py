def find_greatest(a, b, c):
    greatest = a
    if b > greatest:
        greatest = b
    if c > greatest:
        greatest = c
    return greatest

if __name__ == '__main__':
    val1 = 10
    val2 = 45
    val3 = 23
    result = find_greatest(val1, val2, val3)
    print(result)