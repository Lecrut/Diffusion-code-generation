def sum_generator(a, b):
    yield a + b

if __name__ == '__main__':
    sample_value_1 = 5
    sample_value_2 = 10
    for result in sum_generator(sample_value_1, sample_value_2):
        print(result)