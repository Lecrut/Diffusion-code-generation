def get_nth_element(gen, n):
    if n < 0:
        raise ValueError("n must be non-negative")
    count = 0
    for item in gen:
        if count == n:
            return item
        count += 1
    raise IndexError("Generator exhausted before reaching index %d" % n)

if __name__ == '__main__':
    def sample_generator():
        for i in range(1, 10):
            yield i * 10

    gen = sample_generator()
    result = get_nth_element(gen, 3)
    print(result)