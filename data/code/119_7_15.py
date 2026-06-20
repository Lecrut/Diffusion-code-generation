def reverse_order(a: float, b: float) -> (float, float):
    return b, a

if __name__ == '__main__':
    sample_a = 3.14
    sample_b = 2.71
    reversed_result = reverse_order(sample_a, sample_b)
    print(reversed_result)