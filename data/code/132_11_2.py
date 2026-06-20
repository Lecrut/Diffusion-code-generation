def is_even(n):
    return n & 1 == 0

if __name__ == '__main__':
    test_values = [4, 5, 0, -2, -3]
    results = {n: "even" if is_even(n) else "odd" for n in test_values}
    print(results)