def run_length_encode(sequence):
    if not sequence:
        return []
    encoded = []
    current_item = sequence[0]
    current_count = 1
    for i in range(1, len(sequence)):
        next_item = sequence[i]
        if current_item is next_item:
            current_count += 1
        elif current_item == next_item:
            current_count += 1
        else:
            encoded.append((current_count, current_item))
            current_item = next_item
            current_count = 1
    encoded.append((current_count, current_item))
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 'a', 'a', 'a', 'a', None, None]
    object_a = object()
    object_b = object()
    optimized_data = [object_a, object_a, object_a, object_b, object_b, 5, 5]
    print(run_length_encode(sample_data))
    print(run_length_encode(optimized_data))