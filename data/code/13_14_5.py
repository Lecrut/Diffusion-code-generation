def get_generator_value(generator_expression, index):
    iterator = iter(generator_expression)
    for i in range(index + 1):
        value = next(iterator)
    return value

if __name__ == '__main__':
    sample_gen = (x ** 2 for x in range(10))
    result = get_generator_value(sample_gen, 4)
    print(result)