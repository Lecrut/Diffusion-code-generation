def threshold_generator(threshold):
    first_value_received = False
    while True:
        value = (yield)
        if not first_value_received:
            first_value_received = True
            result = value > threshold
            yield result
        else:
            yield False
if __name__ == '__main__':
    threshold_value = 15
    gen = threshold_generator(threshold_value)
    next(gen)
    print(gen.send(10))
    print(gen.send(20))
    print(gen.send(25))