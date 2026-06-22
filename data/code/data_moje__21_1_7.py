def find_maximum(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum

if __name__ == '__main__':
    x = 10
    y = 25
    z = 15
    print(find_maximum(x, y, z))