def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

if __name__ == '__main__':
    x = 30
    y = 15
    z = 25
    result = find_largest(x, y, z)
    print(f"The largest number among {x}, {y}, and {z} is: {result}")