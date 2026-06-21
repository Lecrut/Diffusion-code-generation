def is_odd(n):
    return n & 1 == 1

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, -1, -2, -3]
    results = {n: is_odd(n) for n in sample_values}
    print(results)