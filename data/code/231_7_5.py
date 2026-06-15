def repeating_sequence_generator(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step
if __name__ == '__main__':
    generator = repeating_sequence_generator(0, 20, 3)
    results = list(generator)
    print(results)