def calculate_total_sum(n):
    return n * (n + 1) // 2

if __name__ == '__main__':
    sample_number = 1000
    result = calculate_total_sum(sample_number)
    print(result)