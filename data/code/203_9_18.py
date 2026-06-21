def are_close(num1, num2, tolerance=1e-9):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return abs(num1 - num2) <= tolerance

if __name__ == '__main__':
    try:
        result = are_close(0.1 + 0.2, 0.3)
        print(result)
    except ValueError as e:
        print(f"An error occurred during comparison: {e}", file=sys.stderr)