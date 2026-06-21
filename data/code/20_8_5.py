def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [-4, -3, -1, 0, 1, 2, 3, 4]
    results = [is_even(n) for n in sample_values]
    print(results)