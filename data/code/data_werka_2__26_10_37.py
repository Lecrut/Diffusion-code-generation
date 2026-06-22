def threshold_generator(threshold):
    value = (yield)
    while True:
        if value > threshold:
            yield True
        else:
            yield False
        value = (yield)
if __name__ == '__main__':
    gen = threshold_generator(10)
    next(gen)
    values = [5, 15, 20, 8, 12]
    results = []
    for value in values:
        results.append(gen.send(value))
    print(results)