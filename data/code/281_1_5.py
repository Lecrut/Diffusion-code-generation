def sum_and_round(num1, num2, num3, num4):
    total = num1 + num2 + num3 + num4
    return round(total, 2)

if __name__ == '__main__':
    sample_values = [3.14159, 2.71828, 0.61803, 1.41421]
    result = sum_and_round(*sample_values)
    print(result)