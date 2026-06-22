def sum_with_precision(a: float, b: float) -> float:
    return round(a + b, 15)

if __name__ == '__main__':
    result = sum_with_precision(0.1, 0.2)
    print(result)