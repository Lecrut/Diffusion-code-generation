def validate_numbers(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")

def sum_three_numbers(a, b, c):
    validate_numbers(a, b, c)
    return a + b + c

if __name__ == '__main__':
    result = sum_three_numbers(10, 20, 30)
    print(result)