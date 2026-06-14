def infinite_sequence_stopper(stop_count):
    sequence = ['X', 'Y']
    count = 0
    while True:
        if count >= stop_count:
            break
        yield sequence[count % len(sequence)]
        count += 1
if __name__ == '__main__':
    stop_value = 10
    generator = infinite_sequence_stopper(stop_value)
    result = []
    for item in generator:
        result.append(item)
        if len(result) >= stop_value:
            break
    print(result)