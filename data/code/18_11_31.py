def threshold_generator(threshold):
    first = True
    while True:
        value = (yield)
        if first:
            result = value > threshold
            first = False
        else:
            result = False
        yield result
if __name__ == '__main__':
    gen = threshold_generator(10)
    next(gen)
    print(gen.send(5))
    print(gen.send(15))
    print(gen.send(20))