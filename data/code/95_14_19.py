def check_conditions(a: float, b: float, c: float) -> bool:
    return a > 0 and b < a and (c == a + b)
if __name__ == '__main__':
    print(check_conditions(5.0, 2.0, 7.0))
    print(check_conditions(-1.0, -2.0, -3.0))