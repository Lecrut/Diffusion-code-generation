def get_nth_from_generator(generator, n):
    if n < 0:
        raise ValueError("n must be non-negative")
    try:
        for i, value in enumerate(generator):
            if i == n:
                return value
        return None
    except TypeError:
        raise TypeError("The provided argument is not a generator")

if __name__ == '__main__':
    def sample_gen():
        yield 10
        yield 20
        yield 30
        yield 40

    result = get_nth_from_generator(sample_gen(), 2)
    print(result)