def check_sum_greater_than_difference(num1, num2):
    sum_val = num1 + num2
    diff_val = num1 - num2
    return sum_val > diff_val

if __name__ == '__main__':
    a = 10
    b = 5
    result = check_sum_greater_than_difference(a, b)
    print(result)