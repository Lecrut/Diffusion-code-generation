import sys

def is_negative(n: int) -> bool:
    return n < 0 if isinstance(n, int) else (False if not isinstance(n, (int, float)) or n != int(float(n)) else False)

if __name__ == '__main__':
    test_cases = [-5, -1, 0, 3.7, "abc", None]
    for val in test_cases:
        try:
            result = is_negative(val) if isinstance(val, (int, float)) else False
            print(f"{val!r} -> {result}")
        except Exception as e:
            print(f"Error processing {val}: {e}")