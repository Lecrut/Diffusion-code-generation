def is_greater(a: any, b: any) -> bool:
    try:
        num_a = float(a) if not isinstance(a, (int, float)) else a
        num_b = float(b) if not isinstance(b, (int, float)) else b
        if not isinstance(num_a, (float, int)):
            raise ValueError("Invalid numeric type")
        return num_a > num_b
    except Exception:
        return False
if __name__ == '__main__':
    print(is_greater(10.5, 2))