def is_greater(a: object, b: object) -> bool:
    try:
        na = float(a) if not isinstance(a, (int, float)) else a
        nb = float(b) if not isinstance(b, (int, float)) else b
        return na > nb
    except (TypeError, ValueError):
        raise TypeError("Both arguments must be numeric types")
if __name__ == '__main__':
    print(is_greater(10.5, 20))