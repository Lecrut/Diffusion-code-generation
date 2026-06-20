NUMERIC_TYPE = (int, float)

def multiply_numbers(a: NUMERIC_TYPE, b: NUMERIC_TYPE) -> float:
    return float(a * b)

if __name__ == '__main__':
    result = multiply_numbers(4.5, 2)
    print(result)