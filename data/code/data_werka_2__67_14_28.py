def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be either integers or floating-point numbers.')

def compute_sum(a, b):
    validate_numbers(a, b)
    return a + b
if __name__ == '__main__':
    sample_values = [(5, 3), (2.5, 4.7), (-1, -1), (0, 0), (100, 200.5)]
    for num1, num2 in sample_values:
        result = compute_sum(num1, num2)
        print(f'Result of adding {num1} and {num2}: {result}')