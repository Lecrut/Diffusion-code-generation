def sum_generator(a, b):
    total = a + b
    yield total

if __name__ == '__main__':
    first_number = 7.5
    second_number = 2.5
    result = next(sum_generator(first_number, second_number))
    print(result)