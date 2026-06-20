def is_odd(n):
    return n & 1 == 1

if __name__ == '__main__':
    samples = [3, 4, 5, 6]
    results = {n: is_odd(n) for n in samples}
    print(results)