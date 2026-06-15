def multiply_and_divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    result = dividend / divisor
    product = dividend * divisor
    return result, product
if __name__ == '__main__':
    dividend1 = 10
    divisor1 = 2
    try:
        result1, product1 = multiply_and_divide(dividend1, divisor1)
        print(f"Dividend: {dividend1}, Divisor: {divisor1}")
        print(f"Division result: {result1}")
        print(f"Multiplication result: {product1}")
    except ValueError as e:
        print(f"Error: {e}")
    dividend2 = 15
    divisor2 = 3
    try:
        result2, product2 = multiply_and_divide(dividend2, divisor2)
        print(f"\nDividend: {dividend2}, Divisor: {divisor2}")
        print(f"Division result: {result2}")
        print(f"Multiplication result: {product2}")
    except ValueError as e:
        print(f"Error: {e}")
    dividend3 = 7
    divisor3 = 0
    try:
        result3, product3 = multiply_and_divide(dividend3, divisor3)
        print(f"\nDividend: {dividend3}, Divisor: {divisor3}")
        print(f"Division result: {result3}")
        print(f"Multiplication result: {product3}")
    except ValueError as e:
        print(f"\nError: {e}")