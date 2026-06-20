def calculate(a, b):
    return a + b, a - b

if __name__ == '__main__':
    result_add, result_sub = calculate(10, 5)
    print(result_add)
    print(result_sub)