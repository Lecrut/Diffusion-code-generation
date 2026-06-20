def validate_arguments(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All arguments must be numbers")

def sum_three_numbers(a, b, c):
    validate_arguments(a, b, c)
    return a + b + c

if __name__ == '__main__':
    result = sum_three_numbers(10, 20, 30)
    print(result)