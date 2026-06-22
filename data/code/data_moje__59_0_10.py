def sum_of_digits(n: int) -> int:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    sample_values = [123, 4567, 9999, 0, 100000]
    results = [sum_of_digits(val) for val in sample_values]
    for val, res in zip(sample_values, results):
        print(f"sum_of_digits({val}) = {res}")