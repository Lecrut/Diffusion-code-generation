def is_greater(a: object, b: object) -> bool:
    try:
        a_num = float(a) if not isinstance(a, (int, float)) else a
        b_num = float(b) if not isinstance(b, (int, float)) else b
        if not (isinstance(a_num, (int, float)) and isinstance(b_num, (int, float))):
            return False
        return a_num > b_num
    except (ValueError, TypeError):
        return False
if __name__ == '__main__':
    print(is_greater(10.5, 9))