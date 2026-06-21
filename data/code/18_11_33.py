def threshold_generator(threshold):
    first = True

    def validate_value(value):
        if not isinstance(value, (int, float)):
            raise ValueError('Input must be an integer or a float.')
    while True:
        value = (yield)
        if first:
            validate_value(value)
            result = value > threshold
            first = False
            yield result
        else:
            yield False
if __name__ == '__main__':
    gen = threshold_generator(10)
    next(gen)
    print(gen.send(5))
    print(gen.send(15))
    print(gen.send(20))