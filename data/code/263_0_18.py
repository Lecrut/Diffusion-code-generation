def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

if __name__ == '__main__':
    x = 42
    y = 17
    z = 33
    result = find_largest(x, y, z)
    print(f"The largest number among {x}, {y}, and {z} is: {result}")