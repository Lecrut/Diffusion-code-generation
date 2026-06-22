def check_sum_greater_than_difference(a, b):
    s = a + b
    d = a - b
    return s > d

if __name__ == '__main__':
    x = 10
    y = 5
    result = check_sum_greater_than_difference(x, y)
    print(result)