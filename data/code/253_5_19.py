def find_middle_value(a, b, c):
    if a < b:
        return b if b < c else min(a, c)
    return a if a < c else min(b, c)

if __name__ == '__main__':
    print(find_middle_value(3, 1, 2))
    print(find_middle_value(5, 9, 7))
    print(find_middle_value(-1, -3, -2))