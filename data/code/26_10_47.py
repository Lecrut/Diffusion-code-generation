def threshold_generator(threshold):
    while True:
        value = yield
        if value > threshold:
            yield True
        else:
            yield False

if __name__ == '__main__':
    gen = threshold_generator(10)
    next(gen)
    values = [2, 13, 6, 18, 5]
    results = []
    for val in values:
        results.append(gen.send(val))
    print(results)