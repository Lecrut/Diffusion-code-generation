def infinite_sequence_limited(sequence):
    count = 0
    while True:
        yield sequence[count % len(sequence)]
        count += 1
if __name__ == '__main__':
    sample_sequence = 'X, Y'
    limit = 10
    generator = infinite_sequence_limited(sample_sequence)
    results = []
    for _ in range(limit):
        results.append(next(generator))
    print(results)