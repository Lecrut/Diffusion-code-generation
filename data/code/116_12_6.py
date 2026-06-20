def sum_floats(a: float, b: float, c: float) -> float:
    return a + b + c

if __name__ == '__main__':
    result = sum_floats(1.0e307, 2.0e-308, -1.0e307)
    print(result)