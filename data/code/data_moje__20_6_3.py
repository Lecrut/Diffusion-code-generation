def is_even(n):
    return (n & 1) == 0

if __name__ == '__main__':
    values = [0, 1, 2, 3, 4, 100, 101, 500]
    results = [is_even(x) for x in values]
    print(results)