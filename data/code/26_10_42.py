THRESHOLD_VALUE = 10

def threshold_generator(threshold):
    while True:
        value = yield
        if value > threshold:
            yield True
        else:
            yield False

if __name__ == '__main__':
    gen = threshold_generator(THRESHOLD_VALUE)
    next(gen)
    test_values = [7, 13, 9, 20, 5]
    results = []
    for value in test_values:
        results.append(gen.send(value))
    print(results)