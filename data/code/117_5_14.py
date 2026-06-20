NUMERIC_TYPES = (int, float)

def calculate_difference(num1: float, num2: float) -> float:
    if not all(isinstance(n, NUMERIC_TYPES) for n in (num1, num2)):
        raise TypeError("Both arguments must be numeric")
    return num1 - num2

if __name__ == '__main__':
    result = calculate_difference(100.5, 45.2)
    print(result)