import sys
def safe_divide(a: float, b: float) -> float | None:
    try:
        if b == 0:
            return None
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Zero division error occurred: {e}", file=sys.stderr)
        raise
if __name__ == '__main__':
    num1 = 10.5
    num2 = 4
    if safe_divide(num1, num2) is None:
        sys.exit(1)