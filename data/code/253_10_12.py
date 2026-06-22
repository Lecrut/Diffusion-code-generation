def is_valid_number(value):
    return isinstance(value, (int, float))

def find_the_middle_value_among_three_calculate(a, b, c):
    if not all(is_valid_number(x) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    
    numbers = sorted([a, b, c])
    return numbers[1]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_calculate(1, 2, 3))
    print(find_the_middle_value_among_three_calculate(3, 1, 2))
    print(find_the_middle_value_among_three_calculate(5, 2, 8))
    print(find_the_middle_value_among_three_calculate(-10, 0, 5))
    print(find_the_middle_value_among_three_calculate(100, 100, 100))