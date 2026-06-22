def validate_inputs(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise ValueError("All inputs must be numbers.")
    return a, b, c

def find_the_middle_value_among_three_calculate(a, b, c):
    a, b, c = validate_inputs(a, b, c)
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return b

if __name__ == '__main__':
    print(find_the_middle_value_among_three_calculate(1, 2, 3))
    print(find_the_middle_value_among_three_calculate(3, 1, 2))
    print(find_the_middle_value_among_three_calculate(5, 2, 8))
    print(find_the_middle_value_among_three_calculate(-10, 0, 5))
    print(find_the_middle_value_among_three_calculate(100, 100, 100))