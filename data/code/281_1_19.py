def calculate_sum(num1, num2, num3, num4):
    return round(num1 + num2 + num3 + num4, 2)

if __name__ == '__main__':
    sample_values = (1.2345, 6.7890, 2.3456, 3.4567)
    result = calculate_sum(*sample_values)
    print(result)