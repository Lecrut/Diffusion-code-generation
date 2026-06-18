import sys
def calculate_sum(a: int | float = 0, b: int | float = 0, c: int | float = 0) -> float:
    try:
        return a + b + c
    except TypeError as e:
        raise ValueError("All arguments must be numeric.") from e
if __name__ == '__main__':
    x = 10.5
    y = -3
    z = "not_a_number"
    try:
        total = calculate_sum(x, y, z)
        print(f"The sum is {total}")
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)