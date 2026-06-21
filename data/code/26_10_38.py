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
    values = [3, 11, 7, 25, 9]
    results = []
    for value in values:
        results.append(gen.send(value))
    print(results)