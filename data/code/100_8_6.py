def check_sum_and_difference(a, b):
    return a + b > abs(a - b)

if __name__ == '__main__':
    result = check_sum_and_difference(5, 3)
    print(result)