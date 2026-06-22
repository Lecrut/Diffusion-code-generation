def find_max_of_three(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum

if __name__ == '__main__':
    x = 15
    y = 42
    z = 7
    print(find_max_of_three(x, y, z))