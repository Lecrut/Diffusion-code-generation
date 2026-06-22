def run_length_encode(sequence):
    if not sequence:
        return []
    result = []
    current_item = sequence[0]
    count = 1
    for item in sequence[1:]:
        if item == current_item:
            count += 1
        else:
            result.append((current_item, count))
            current_item = item
            count = 1
    result.append((current_item, count))
    return result

if __name__ == '__main__':
    sample_sequence = "AAABBBCCDAA"
    encoded = run_length_encode(sample_sequence)
    print(encoded)
    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    encoded_list = run_length_encode(sample_list)
    print(encoded_list)
    empty_sequence = []
    encoded_empty = run_length_encode(empty_sequence)
    print(encoded_empty)
    single_element = ['x']
    encoded_single = run_length_encode(single_element)
    print(encoded_single)