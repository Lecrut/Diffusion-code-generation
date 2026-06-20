def calculate_sum_and_difference(a: int, b: int) -> (int, int):
    return a + b, a - b

if __name__ == '__main__':
    sample_a = 20
    sample_b = 8
    result = calculate_sum_and_difference(sample_a, sample_b)
    print(result)