import sys
def add(a: float | int = 0, b: float | int = 0) -> float | int:
    try:
        a_val = float(a) if not isinstance(a, (int, float)) else a
        b_val = float(b) if not isinstance(b, (int, float)) else b
        return a_val + b_val
    except ValueError as e:
        print(f"Error during addition: {e}", file=sys.stderr)
        sys.exit(1)
if __name__ == '__main__':
    result = add(a=50.25, b=73.89)
    print(result)