def repeating_sequence_generator(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step
if __name__ == '__main__':
    for num in repeating_sequence_generator(0, 20, 3):
        print(num)