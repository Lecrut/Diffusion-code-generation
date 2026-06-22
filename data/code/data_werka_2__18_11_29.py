THRESHOLD = 10

def threshold_generator(threshold):
    first_value_received = False
    while True:
        value = (yield)
        if not first_value_received:
            first_value_received = True
            yield (value > threshold)
        else:
            yield False
if __name__ == '__main__':
    gen = threshold_generator(THRESHOLD)
    next(gen)
    print(gen.send(5))
    print(gen.send(15))
    print(gen.send(20))