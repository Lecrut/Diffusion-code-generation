def check_sum_greater_than_difference(a, b):
    sum_val = a + b
    diff_val = a - b
    return sum_val > diff_val

if __name__ == '__main__':
    x = 10
    y = 5
    result = check_sum_greater_than_difference(x, y)
    print(result)