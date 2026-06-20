def check_conditions(a: float, b: float, c: float) -> bool:
    if not all((isinstance(i, (int, float)) for i in [a, b, c])):
        raise ValueError('All parameters must be numbers')
    return a > 0 and b < a and (c == a + b)
if __name__ == '__main__':
    print(check_conditions(5.0, 3.0, 8.0))
    print(check_conditions(-1.0, 2.0, 3.0))
    print(check_conditions(4.0, 4.0, 8.0))