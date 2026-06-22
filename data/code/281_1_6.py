def sum_and_round(num1, num2, num3, num4):
    total = num1 + num2 + num3 + num4
    return round(total, 2)

if __name__ == '__main__':
    result = sum_and_round(1.2345, 6.7890, 2.3456, 3.4567)
    print(result)