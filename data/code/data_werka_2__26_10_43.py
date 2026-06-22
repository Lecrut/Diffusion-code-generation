def threshold_generator(threshold):
    while True:
        value = yield
        if value > threshold:
            yield True
        else:
            yield False

if __name__ == '__main__':
    gen = threshold_generator(5)
    next(gen)
    test_values = [1, 6, 3, 7, 2]
    results = []
    for val in test_values:
        result = gen.send(val)
        results.append(result)
    print(results)