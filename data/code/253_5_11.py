def find_middle_value(a, b, c):
    values = [a, b, c]
    if len(values) != 3:
        raise ValueError("Input must be exactly three numbers.")
    return sorted(values)[1]

if __name__ == '__main__':
    print(find_middle_value(3, 1, 2))
    print(find_middle_value(5, 9, 7))
    print(find_middle_value(-1, -3, -2))