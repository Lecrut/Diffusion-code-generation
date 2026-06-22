def is_even(n):
    return (n & 1) == 0

if __name__ == '__main__':
    results = []
    for val in [4, 7, 0, -2]:
        results.append(is_even(val))
    print(results)