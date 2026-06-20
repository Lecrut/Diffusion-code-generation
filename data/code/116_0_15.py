def validate_inputs(a, b, c):
    if not all(isinstance(x, int) for x in [a, b, c]):
        raise ValueError("All inputs must be integers.")
    if any(x < 0 for x in [a, b, c]):
        raise ValueError("Inputs must be non-negative.")

def calculate_sum(a, b, c):
    validate_inputs(a, b, c)
    return a + b + c

if __name__ == '__main__':
    num1 = 10
    num2 = 20
    num3 = 30
    result = calculate_sum(num1, num2, num3)
    print(result)