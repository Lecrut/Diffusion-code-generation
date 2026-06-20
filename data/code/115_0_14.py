def safe_divide(dividend: float, divisor: float) -> float:
    if divisor == 0:
        return float('nan')
    else:
        return dividend / divisor

if __name__ == '__main__':
    division_results = {
        (10.0, 2.0): safe_divide(10.0, 2.0),
        (5.0, 0.0): safe_divide(5.0, 0.0)
    }
    
    for (numerator, denominator), result in division_results.items():
        print(f"Division of {numerator} by {denominator}: {result}")