def validate_numbers(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    return a, b, c

def sum_three_numbers(a, b, c):
    validated_values = validate_numbers(a, b, c)
    return sum(validated_values)

if __name__ == '__main__':
    result = sum_three_numbers(10, 20, 30)
    print(result)