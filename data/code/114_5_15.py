NUMERIC_TYPES = (int, float)

def multiply_numbers(a: NUMERIC_TYPES, b: NUMERIC_TYPES) -> float:
    return float(a * b)

if __name__ == '__main__':
    result = multiply_numbers(3.5, 2)
    print(result)