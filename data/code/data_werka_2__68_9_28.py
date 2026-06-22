def validate_numbers(num1, num2):
    if not isinstance(num1, (int, float)):
        raise ValueError(f'First input must be a number, got {type(num1).__name__}')
    if not isinstance(num2, (int, float)):
        raise ValueError(f'Second input must be a number, got {type(num2).__name__}')

def find_difference(num1, num2):
    validate_numbers(num1, num2)
    return abs(num1 - num2)
if __name__ == '__main__':
    sample_values = [(10, 4), (-5, 15), (7.5, 3.2), (0, 0), ('a', 5)]
    for a, b in sample_values:
        try:
            result = find_difference(a, b)
            print(f'The absolute difference between {a} and {b} is: {result}')
        except ValueError as e:
            print(e)