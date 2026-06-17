import sys
def divide_numbers(initial: float = 100.0, divisor: float = 2) -> tuple[float, int]:
    try:
        result = initial / divisor
        return (result, 0)
    except ZeroDivisionError:
        return (-float('inf'), -1)
if __name__ == '__main__':
    res, status = divide_numbers(256.0, 8.0)
    if status >= 0:
        print(f"Result: {res}")