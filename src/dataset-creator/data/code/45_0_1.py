import sys
def safe_sum(a: float, b: float) -> int | None:
    try:
        a_int = int(a)
        b_int = int(b)
        return a_int + b_int
    except ValueError as e:
        print(f"Error: Invalid input. {e}")
        sys.exit(1)
if __name__ == '__main__':
    num_1 = 5
    num_2 = 3
    result = safe_sum(num_1, num_2)
    if result is not None:
        print(f"Sum of {num_1} and {num_2}: {result}")