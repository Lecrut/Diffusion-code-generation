def sum_generator(a, b):
    yield a + b

if __name__ == '__main__':
    SAMPLE_A = 10
    SAMPLE_B = 20
    result = next(sum_generator(SAMPLE_A, SAMPLE_B))
    print(result)