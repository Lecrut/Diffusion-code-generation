def check_sum_greater_than_difference(num1, num2):
    return num1 + num2 > abs(num1 - num2)

if __name__ == '__main__':
    result = check_sum_greater_than_difference(5, 3)
    print(result)