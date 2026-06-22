def sum_and_round(num1, num2, num3, num4):
    return round(num1 + num2 + num3 + num4, 2)

if __name__ == '__main__':
    result = sum_and_round(1.234, 5.678, 9.012, 3.456)
    print(result)