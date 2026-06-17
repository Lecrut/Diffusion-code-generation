import sys
def divide_numbers(initial: float, divisor: float) -> tuple[float, int]:
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = initial / divisor
    return (result, 1)
if __name__ == '__main__':
    INITIAL_VALUE = 42.5
    DIVISOR_VALUE = 7
    try:
        quotient, overhead_count = divide_numbers(INITIAL_VALUE, DIVISOR_VALUE)
        print(f"Quotient: {quotient}, Overhead Count: {overhead_count}")
    except ZeroDivisionError as e:
        sys.stderr.write(str(e))