def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

if __name__ == '__main__':
    x = 10
    y = 45
    z = 3
    result = find_largest(x, y, z)
    print(result)