def sum_generator(a: float, b: float) -> float:
    yield a + b

if __name__ == '__main__':
    SAMPLE_VALUE_A = 3.14159
    SAMPLE_VALUE_B = 2.71828
    result = next(sum_generator(SAMPLE_VALUE_A, SAMPLE_VALUE_B))
    print(result)