def threshold_generator(threshold):
    while True:
        value = yield
        if value > threshold:
            yield True
        else:
            yield False

if __name__ == '__main__':
    gen = threshold_generator(15)
    next(gen)
    values = [20, 10, 25, 14, 30]
    results = []
    for value in values:
        results.append(gen.send(value))
    print(results)