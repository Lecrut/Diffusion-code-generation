def infinite_sequence_limiter(sequence):
    count = 0
    while True:
        yield sequence[count % len(sequence)]
        count += 1
if __name__ == '__main__':
    target_count = 10
    generator = infinite_sequence_limiter('X, Y')
    result = []
    for item in generator:
        result.append(item)
        if len(result) >= target_count:
            break
    print(result)