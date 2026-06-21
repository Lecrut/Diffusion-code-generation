def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [4, 7, 0, -3, 100]
    results = [is_even(n) for n in sample_values]
    for n, result in zip(sample_values, results):
        print(f"is_even({n}) = {result}")