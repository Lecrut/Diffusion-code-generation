def sum_generator(a, b):
    yield a + b

if __name__ == '__main__':
    first_value = 15.5
    second_value = 24.3
    total = next(sum_generator(first_value, second_value))
    print(total)