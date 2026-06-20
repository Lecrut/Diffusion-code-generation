def check_conditions(a: float, b: float, c: float) -> bool:
    return a > 0 and b < a and (c == a + b)
if __name__ == '__main__':
    print(check_conditions(3.5, 2.1, 5.6))