def infinite_sequence_limited(start_sequence, limit):
    sequence = list(start_sequence)
    index = 0
    while True:
        if index >= len(sequence):
            yield sequence[index % len(sequence)]
        else:
            yield sequence[index]
        index += 1
        if index >= limit:
            break
if __name__ == '__main__':
    start = ['X', 'Y']
    limit = 10
    generator = infinite_sequence_limited(start, limit)
    for item in generator:
        print(item)