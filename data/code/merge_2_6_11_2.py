def is_greater(a: object, b: object) -> bool:
    try:
        numeric_a = float(a) if not isinstance(a, (int, float)) else a
        numeric_b = float(b) if not isinstance(b, (int, float)) else b
        if not isinstance(numeric_a, (float, int)):
            raise ValueError("Invalid input type for 'a'")
        if not isinstance(numeric_b, (float, int)):
            raise ValueError("Invalid input type for 'b'")
        return numeric_a > numeric_b
    except Exception:
        return False
if __name__ == '__main__':
    print(is_greater(10.5, 7))