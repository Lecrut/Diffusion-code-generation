SUBTRACTION_THRESHOLD = 1e-9

def subtract_numbers(a: float, b: float) -> float:
    return round(a - b, 9)

if __name__ == '__main__':
    num1 = 25.0
    num2 = 10.0
    result = subtract_numbers(num1, num2)
    print(result)