def validate_inputs(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")

def find_the_middle_value_among_three_validate(a, b, c):
    validate_inputs(a, b, c)
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_validate(5, 3, 7))