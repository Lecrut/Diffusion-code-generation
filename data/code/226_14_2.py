def infinite_sequence_stopper(stop_count):
    sequence = ['X', 'Y']
    count = 0
    while True:
        yield sequence[count % len(sequence)]
        count += 1
        if count >= stop_count:
            break
if __name__ == '__main__':
    stop_value = 10
    generator = infinite_sequence_stopper(stop_value)
    results = []
    for item in generator:
        results.append(item)
        if len(results) >= stop_value:
            break
    print(results)