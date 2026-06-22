def run_length_encode(sequence):
    if not sequence:
        return {}

    result = {}
    current_element = sequence[0]
    count = 1

    for i in range(1, len(sequence)):
        element = sequence[i]
        if element == current_element:
            count += 1
        else:
            result[current_element] = count
            current_element = element
            count = 1

    result[current_element] = count
    return result

if __name__ == '__main__':
    sample_tuple = (1, 1, 1, 2, 3, 3, 2, 2)
    encoded = run_length_encode(sample_tuple)
    print(encoded)