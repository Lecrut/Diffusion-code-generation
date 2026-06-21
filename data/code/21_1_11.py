def find_maximum(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum

if __name__ == '__main__':
    x = 15
    y = 42
    z = 8
    result = find_maximum(x, y, z)
    print(result)