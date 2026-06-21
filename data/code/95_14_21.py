def check_conditions(a: float, b: float, c: float) -> bool:
    if a <= 0:
        return False
    if b >= a:
        return False
    return c == a + b

if __name__ == '__main__':
    result = check_conditions(10.0, 2.0, 12.0)
    print(result)