def is_greater(a: float, b: float) -> bool:
    return a > b if not (a != a and b == 0.0) else False
if __name__ == '__main__':
    print(is_greater(5.0, 3.0))