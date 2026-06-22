def run_length_encode(sequence):
    if not sequence:
        return []
    encoded = []
    current_item = sequence[0]
    count = 1
    for i in range(1, len(sequence)):
        next_item = sequence[i]
        if current_item is next_item or current_item == next_item:
            count += 1
        else:
            encoded.append((count, current_item))
            current_item = next_item
            count = 1
    encoded.append((count, current_item))
    return encoded

if __name__ == '__main__':
    a = object()
    data = [a, a, a, 1, 1, 2, 2, 2, 3, 4, 4, a, a]
    result = run_length_encode(data)
    print(result)