def is_greater(a: object, b: object) -> bool:
    try:
        val_a = float(a) if not isinstance(a, (int, float)) else a
        val_b = float(b) if not isinstance(b, (int, float)) else b
        if not isinstance(val_a, (int, float)) or not isinstance(val_b, (int, float)):
            return False
        return val_a > val_b
    except (ValueError, TypeError):
        return False
if __name__ == '__main__':
    print(is_greater(10.5, 9))