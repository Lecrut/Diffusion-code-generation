def repeating_generator(start, step):
    current = start
    while True:
        yield current
        current += step
if __name__ == '__main__':
    start_value = 0
    step_size = 3
    generator = repeating_generator(start_value, step_size)
    sequence = []
    for i in range(10):
        sequence.append(next(generator))
    print(sequence)