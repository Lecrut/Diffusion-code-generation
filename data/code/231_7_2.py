def repeating_sequence_generator(start, end, step):
    current = start
    while current <= end:
        yield current
        current += step
if __name__ == '__main__':
    for num in repeating_sequence_generator(0, 100, 10):
        print(num)