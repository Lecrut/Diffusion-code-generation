def threshold_generator(threshold):
    if not isinstance(threshold, (int, float)):
        raise ValueError('Threshold must be an integer or a float.')
    first_value_received = False
    while True:
        value = (yield)
        if not first_value_received:
            first_value_received = True
            yield (value > threshold)
        else:
            yield False
if __name__ == '__main__':
    try:
        gen = threshold_generator(10)
        next(gen)
        print(gen.send(5))
        print(gen.send(15))
        print(gen.send(20))
    except ValueError as e:
        print(e)