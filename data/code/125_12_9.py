def calculate(a, b):
    return a + b, a - b

if __name__ == '__main__':
    result_sum, result_diff = calculate(5, 3)
    print(result_sum)
    print(result_diff)