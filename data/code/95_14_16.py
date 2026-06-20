def check_conditions(a: float, b: float, c: float) -> bool:
    return a > 0 and b < a and c == a + b

if __name__ == '__main__':
    result = check_conditions(5.0, 3.0, 8.0)
    print(result)