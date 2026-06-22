def get_nth(generator, n):
    for i, value in enumerate(generator):
        if i == n:
            return value
    return None

if __name__ == '__main__':
    def sample_gen():
        for i in range(10):
            yield i * 10

    result = get_nth(sample_gen(), 3)
    print(result)