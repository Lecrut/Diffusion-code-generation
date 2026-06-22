def find_middle_value(a, b, c):
    values = [a, b, c]
    values.sort()
    return values[1]

if __name__ == '__main__':
    x = 4
    y = 2
    z = 3
    print(find_middle_value(x, y, z))