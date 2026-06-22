def run_length_encode(sequence):
    if not sequence:
        return []
    result = []
    current_value = sequence[0]
    count = 1
    for item in sequence[1:]:
        if item is current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = item
            count = 1
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample = ['a', 'a', 'a', 'b', 'b', 'c', 'd', 'd', 'd', 'd']
    encoded = run_length_encode(sample)
    print(encoded)