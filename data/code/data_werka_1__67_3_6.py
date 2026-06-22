def sum_generator(a, b):
    yield a + b

if __name__ == '__main__':
    sample_a = 5
    sample_b = 3
    result = next(sum_generator(sample_a, sample_b))
    print(result)