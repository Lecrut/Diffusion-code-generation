def sum_and_round(num1: float, num2: float, num3: float, num4: float) -> float:
    return round(num1 + num2 + num3 + num4, 2)

if __name__ == '__main__':
    result = sum_and_round(1.2345, 6.7890, 2.3456, 3.4567)
    print(result)