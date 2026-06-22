def calculate_sum_and_round(num1, num2, num3, num4):
    total = num1 + num2 + num3 + num4
    return round(total, 2)

if __name__ == '__main__':
    sample_values = {
        'num1': 1.2345,
        'num2': 6.7890,
        'num3': 2.3456,
        'num4': 3.4567
    }
    result = calculate_sum_and_round(**sample_values)
    print(result)