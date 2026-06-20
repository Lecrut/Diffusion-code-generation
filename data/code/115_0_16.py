def divide_numbers(dividend: float, divisor: float) -> float:
    if divisor == 0:
        return None
    return dividend / divisor

if __name__ == '__main__':
    result = divide_numbers(10.0, 2.0)
    print(result)
    result = divide_numbers(5.0, 0.0)
    print(result)