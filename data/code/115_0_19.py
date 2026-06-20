def safe_divide(dividend: float, divisor: float) -> float:
    if divisor == 0:
        return None
    else:
        return dividend / divisor

if __name__ == '__main__':
    operations = {
        '10/2': (10.0, 2.0),
        '5/0': (5.0, 0.0)
    }

    for description, (numerator, denominator) in operations.items():
        result = safe_divide(numerator, denominator)
        print(f'{description} -> {result}')