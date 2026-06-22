def threshold_generator(threshold):
    if not isinstance(threshold, (int, float)):
        raise ValueError('Threshold must be an integer or float.')
    first = True
    while True:
        try:
            value = (yield)
            if first:
                first = False
                yield (value > threshold)
            else:
                yield False
        except GeneratorExit:
            break
if __name__ == '__main__':
    threshold_value = 10
    gen = threshold_generator(threshold_value)
    next(gen)
    print(gen.send(5))
    print(gen.send(15))
    print(gen.send(20))