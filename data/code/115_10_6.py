def divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')

if __name__ == '__main__':
    print(divide(20.5, 4.2))