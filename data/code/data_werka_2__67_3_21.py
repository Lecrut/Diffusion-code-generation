def sum_generator(a, b):
    total = a + b
    yield total

if __name__ == '__main__':
    first_value = 15
    second_value = 20
    result = next(sum_generator(first_value, second_value))
    print(result)