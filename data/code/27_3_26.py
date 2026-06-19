def are_numbers_different(a, b):
    yield a != b

if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result_generator = are_numbers_different(num1, num2)
    print(next(result_generator))