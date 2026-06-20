def calculate_total_sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    return n * (n + 1) // 2

if __name__ == '__main__':
    sample_value = 1000
    result = calculate_total_sum(sample_value)
    print(result)