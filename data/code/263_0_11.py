def find_largest(a, b, c):
    return max(a, b, c)

if __name__ == '__main__':
    sample_a = 10
    sample_b = 25
    sample_c = 15
    largest = find_largest(sample_a, sample_b, sample_c)
    print(f"The largest number among {sample_a}, {sample_b}, and {sample_c} is: {largest}")