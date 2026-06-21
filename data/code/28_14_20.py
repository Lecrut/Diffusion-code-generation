def run_length_encode(sequence):
    if not sequence:
        return []
    result = []
    current_item = sequence[0]
    count = 1
    for item in sequence[1:]:
        if item is current_item:
            count += 1
        else:
            result.append((current_item, count))
            current_item = item
            count = 1
    result.append((current_item, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
    print(run_length_encode(sample_data))
    sample_objects = [object(), object(), [1, 2], [1, 2], [1, 2], "a", "a", "b"]
    print(run_length_encode(sample_objects))
    single_item = [42]
    print(run_length_encode(single_item))
    empty_sequence = []
    print(run_length_encode(empty_sequence))