def check_sum_greater_than_difference(a, b):
    return (a + b) > (a - b)

if __name__ == '__main__':
    x = 5
    y = 3
    result = check_sum_greater_than_difference(x, y)
    print(result)