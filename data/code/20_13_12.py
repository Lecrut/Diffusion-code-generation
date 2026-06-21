def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, -3, 4, 5, 10, 15, 100, 101]
    results = [is_even(n) for n in sample_values]
    for value, even in zip(sample_values, results):
        print(f"{value}: {even}")