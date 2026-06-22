def threshold_generator(threshold):
    while True:
        value = yield
        if value > threshold:
            yield True

if __name__ == '__main__':
    gen = threshold_generator(10)
    next(gen)
    values = [1, 16, 3, 22, 9]
    results = []
    for value in values:
        try:
            result = gen.send(value)
            if result is not None:
                results.append(result)
        except StopIteration:
            break
    print(results)