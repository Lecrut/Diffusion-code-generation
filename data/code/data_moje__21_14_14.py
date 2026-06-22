def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

if __name__ == '__main__':
    val1 = 3.5
    val2 = 7.2
    val3 = 2.8
    result = find_largest(val1, val2, val3)
    print(result)