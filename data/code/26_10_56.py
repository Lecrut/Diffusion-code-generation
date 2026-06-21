THRESHOLD = 10

def threshold_generator(threshold):
    while True:
        value = yield
        if value > threshold:
            yield True
        else:
            yield False

if __name__ == '__main__':
    gen = threshold_generator(THRESHOLD)
    next(gen)
    values = [2, 13, 18, 5, 17]
    results = []
    for value in values:
        results.append(gen.send(value))
    print(results)