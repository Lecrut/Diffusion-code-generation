def is_odd(n):
    return n & 1

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, 16, 31, 64, 127]
    results = {n: is_odd(n) for n in sample_values}
    print(results)