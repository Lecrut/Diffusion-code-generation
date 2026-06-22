def find_the_middle_value_among_three_filter_valid(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise ValueError("All inputs must be numbers")
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    num1 = 7.5
    num2 = 3
    num3 = 9.1
    middle_value = find_the_middle_value_among_three_filter_valid(num1, num2, num3)
    print(middle_value)