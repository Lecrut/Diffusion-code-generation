def reverse_order(a: float, b: float) -> (float, float):
    temp = a
    a = b
    b = temp
    return a, b

if __name__ == '__main__':
    sample_a = 3.14
    sample_b = 2.71
    result = reverse_order(sample_a, sample_b)
    print(result)