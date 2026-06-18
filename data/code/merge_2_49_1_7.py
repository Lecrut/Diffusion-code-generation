def get_sign(value):
    if value is None:
        return 0
    try:
        num = float(value)
        if num == 0:
            return 0
        elif num > 0:
            return 1
        else:
            return -1
    except (ValueError, TypeError):
        return None
if __name__ == '__main__':
    print(get_sign(5))
    print(get_sign(-3.5))
    print(get_sign(0))
    print(get_sign(None))
    print(get_sign("abc"))