def find_the_middle_value_among_three_filter_valid(a, b, c):
    if all(isinstance(n, (int, float)) and n >= 0 for n in [a, b, c]):
        return sorted([a, b, c])[1]
    else:
        raise ValueError("One or more numbers are invalid")

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 15
    middle = find_the_middle_value_among_three_filter_valid(num1, num2, num3)
    print(middle)