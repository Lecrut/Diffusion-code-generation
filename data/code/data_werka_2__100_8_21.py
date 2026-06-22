def check_sum_greater_than_difference(num1, num2):
    total = num1 + num2
    diff = num1 - num2
    return total > diff

if __name__ == '__main__':
    a = 10
    b = 5
    result = check_sum_greater_than_difference(a, b)
    print(result)