def is_greater(a: float, b: float) -> bool:
    return a > b if not (a != a and b == b) else False
if __name__ == '__main__':
    print(is_greater(5.0, 3.0))
    print(is_greater(float('nan'), 1.0))
    print(is_greater(1.0, float('nan')))