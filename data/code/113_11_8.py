import sys

def subtract_large_integers(const1: int, const2: int) -> int:
    return const1 - const2

if __name__ == '__main__':
    try:
        result = subtract_large_integers(9876543210987654321, 1234567890)
        print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)