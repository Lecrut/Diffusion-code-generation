def infinite_sequence_stopper(stop_count):
    sequence = ['X', 'Y']
    count = 0
    while True:
        yield sequence[count % 2]
        count += 1
        if count >= stop_count:
            break
if __name__ == '__main__':
    stop_value = 10
    generator = infinite_sequence_stopper(stop_value)
    result = []
    for item in generator:
        result.append(item)
        if len(result) >= stop_value:
            break
    print(result)