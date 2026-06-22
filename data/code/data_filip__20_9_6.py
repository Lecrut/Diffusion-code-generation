def encode_sequence(sequence):
    if not sequence:
        return []
    encoded = []
    head = sequence[0]
    count = 1
    tail_iter = iter(sequence)
    next(tail_iter)
    for item in tail_iter:
        if item == head:
            count += 1
        else:
            encoded.append((head, count))
            head = item
            count = 1
    encoded.append((head, count))
    return encoded

if __name__ == '__main__':
    sample_input = [7, 7, 7, 8, 8, 9, 9, 9, 9, 1, 1, 2]
    result = encode_sequence(sample_input)
    print(result)