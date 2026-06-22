def find_middle_value(a, b, c):
    values = [a, b, c]
    middle_index = len(values) // 2
    return sorted(values)[middle_index]

if __name__ == '__main__':
    print(find_middle_value(4, 1, 3))
    print(find_middle_value(7, 5, 6))
    print(find_middle_value(-2, -1, -3))