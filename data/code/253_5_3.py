def find_middle_value(a, b, c):
    values = [a, b, c]
    values.sort()
    return values[1]

if __name__ == '__main__':
    print(find_middle_value(4, 2, 3))
    print(find_middle_value(8, 6, 7))
    print(find_middle_value(-5, -4, -3))