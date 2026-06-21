def check_sum_greater_than_difference(num1, num2):
    total = num1 + num2
    diff = num1 - num2
    return total > diff

if __name__ == '__main__':
    result = check_sum_greater_than_difference(10, 5)
    print(result)