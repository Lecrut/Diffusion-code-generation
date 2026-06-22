def find_difference(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError('Both inputs must be numbers')
    return abs(num1 - num2)
if __name__ == '__main__':
    try:
        sample_values = [(10, 4), (-5, 15), (7.5, 3.2), (0, 0), ('a', 5)]
        for a, b in sample_values:
            try:
                result = find_difference(a, b)
                print(f'The absolute difference between {a} and {b} is: {result}')
            except ValueError as e:
                print(f'Error calculating difference for ({a}, {b}): {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')