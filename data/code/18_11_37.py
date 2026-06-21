def validate_threshold(threshold):
    if not isinstance(threshold, (int, float)):
        raise ValueError('Threshold must be an integer or float')

def threshold_generator(threshold):
    validate_threshold(threshold)
    first = True
    while True:
        value = (yield)
        if first:
            result = value > threshold
            first = False
            yield result
        else:
            yield False
if __name__ == '__main__':
    threshold_value = 15
    gen = threshold_generator(threshold_value)
    next(gen)
    print(gen.send(20))
    print(gen.send(10))
    print(gen.send(30))