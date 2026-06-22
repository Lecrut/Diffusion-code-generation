def find_the_middle_value_among_three_filter_valid(a, b, c):
    if all(isinstance(x, (int, float)) for x in [a, b, c]):
        return sorted([a, b, c])[1]
    else:
        raise ValueError('Invalid input: All inputs must be numbers.')

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 15
    middle = find_the_middle_value_among_three_filter_valid(num1, num2, num3)
    print(middle)