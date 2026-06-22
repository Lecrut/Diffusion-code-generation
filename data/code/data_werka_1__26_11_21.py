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
    values_to_test = [5, 15, 20, 8, 12]
    results = [gen.send(value) for value in values_to_test]
    print(results)