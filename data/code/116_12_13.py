def validate_input(a, b, c):
    if not all(isinstance(i, float) for i in [a, b, c]):
        raise TypeError("All inputs must be floats")
    return a, b, c

def sum_floats(a: float, b: float, c: float) -> float:
    validated_values = validate_input(a, b, c)
    result = sum(validated_values)
    return result

if __name__ == '__main__':
    num1 = 1.1
    num2 = 2.2
    num3 = 3.3
    result = sum_floats(num1, num2, num3)
    print(result)