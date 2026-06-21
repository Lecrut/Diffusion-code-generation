def is_even(n: int) -> bool:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Argument must be an integer")
    return (n & 1) == 0

if __name__ == '__main__':
    samples = [4, 7, 0, -3, 2**62]
    results = [is_even(n) for n in samples]
    for n, result in zip(samples, results):
        print(result)