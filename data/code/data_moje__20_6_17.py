def is_even(n):
    return not (n & 1)

if __name__ == '__main__':
    sample_values = [2, 3, 0, -4, 10**9]
    results = [is_even(n) for n in sample_values]
    print(results)