def threshold_generator(threshold):
    first = True
    while True:
        value = (yield)
        if first:
            first = False
            if value > threshold:
                yield True
            else:
                yield False
if __name__ == '__main__':
    gen = threshold_generator(10)
    next(gen)
    print(gen.send(5))
    print(gen.send(15))
    print(gen.send(20))