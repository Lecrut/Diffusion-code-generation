CONST_FACTORIAL_INPUT = 10

def validate_factorial_input(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return n

def compute_factorial_core(n):
    result = 1
    current = 1
    while True:
        result *= current
        current += 1
        if current > n:
            break
    return result

def get_factorial(n):
    validated_n = validate_factorial_input(n)
    return compute_factorial_core(validated_n)

if __name__ == '__main__':
    sample_value = CONST_FACTORIAL_INPUT
    calculated = get_factorial(sample_value)
    print(calculated)