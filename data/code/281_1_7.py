def sum_and_round(num1, num2, num3, num4):
    total = num1 + num2 + num3 + num4
    return round(total, 2)

if __name__ == '__main__':
    result = sum_and_round(1.123, 2.345, 3.456, 4.567)
    print(result)