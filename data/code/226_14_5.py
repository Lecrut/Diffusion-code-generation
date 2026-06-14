def infinite_sequence_limited(start_sequence, limit):
    current_index = 0
    while True:
        yield start_sequence[current_index % len(start_sequence)]
        current_index += 1
        if current_index >= limit:
            break
if __name__ == '__main__':
    sequence = 'X, Y'
    limit = 10
    generator = infinite_sequence_limited(sequence, limit)
    results = []
    for item in generator:
        results.append(item)
        if len(results) >= limit:
            break
    print(results)