SUM_PRECISION = 2

def calculate_sum(num1, num2, num3, num4):
    total = num1 + num2 + num3 + num4
    return round(total, SUM_PRECISION)

if __name__ == '__main__':
    result = calculate_sum(1.2345, 6.7890, 2.3456, 3.4567)
    print(result)