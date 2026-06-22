def find_the_middle_value_among_three_calculate(a, b, c):
    if not all((isinstance(x, (int, float)) for x in [a, b, c])):
        raise ValueError('All inputs must be numbers.')
    if len(set([a, b, c])) != 3:
        raise ValueError('All inputs must be distinct.')
    return sorted([a, b, c])[1]
if __name__ == '__main__':
    print(find_the_middle_value_among_three_calculate(1, 2, 3))
    print(find_the_middle_value_among_three_calculate(5, 1, 4))
    print(find_the_middle_value_among_three_calculate(10, 20, 30))
    print(find_the_middle_value_among_three_calculate(7, 7, 7))