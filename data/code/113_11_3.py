def subtract_amounts(minuend: float, subtrahend: float) -> float:
    return minuend - subtrahend
if __name__ == '__main__':
    result1 = subtract_amounts(100.5, 25.5)
    print(result1)
    result2 = subtract_amounts(50, 150)
    print(result2)
    result3 = subtract_amounts(3.14159, 1.0)
    print(result3)