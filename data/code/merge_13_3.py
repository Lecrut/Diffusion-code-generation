def perform_division(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
if __name__ == '__main__':
    dividend1 = 10
    divisor1 = 2
    result1 = perform_division(dividend1, divisor1)
    print(f"Result of {dividend1} / {divisor1}: {result1}")
    dividend2 = 15
    divisor2 = 3
    result2 = perform_division(dividend2, divisor2)
    print(f"Result of {dividend2} / {divisor2}: {result2}")
    dividend3 = 7
    divisor3 = 0
    result3 = perform_division(dividend3, divisor3)
    print(f"Result of {dividend3} / {divisor3}: {result3}")