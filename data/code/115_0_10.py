def divide_numbers(dividend: float, divisor: float) -> float:
    if divisor == 0:
        return float('nan')
    else:
        return dividend / divisor

if __name__ == '__main__':
    result1 = divide_numbers(8.0, 2.0)
    print(result1)
    
    result2 = divide_numbers(7.0, 0.0)
    print(result2)