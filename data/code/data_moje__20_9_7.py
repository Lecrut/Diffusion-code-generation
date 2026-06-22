def is_even(n):
    return n & 1 == 0

if __name__ == '__main__':
    numbers = [0, 1, 2, 10, 11, 100]
    results = [is_even(n) for n in numbers]
    print(results)