def sum_and_round(num1, num2, num3, num4):
    total_sum = num1 + num2 + num3 + num4
    rounded_result = round(total_sum, 2)
    return rounded_result

if __name__ == '__main__':
    sample_numbers = [1.123, 4.567, 8.901, 2.345]
    result = sum_and_round(*sample_numbers)
    print(result)