def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

if __name__ == '__main__':
    x = 10
    y = 42
    z = 7
    result = find_largest(x, y, z)
    print(result)