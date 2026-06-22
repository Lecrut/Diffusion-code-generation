def find_middle_value(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    print(find_middle_value(3, 1, 2))
    print(find_middle_value(7, 5, 6))
    print(find_middle_value(-1, -2, -3))