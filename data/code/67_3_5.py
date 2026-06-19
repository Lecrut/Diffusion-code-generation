def sum_generator(a, b):
    yield a + b

if __name__ == '__main__':
    num1 = 7.5
    num2 = 4.5
    result = next(sum_generator(num1, num2))
    print(result)