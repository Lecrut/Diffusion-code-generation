def run_length_encode(sequence):
    if not sequence:
        return []

    result = []
    current_value = sequence[0]
    count = 1

    for i in range(1, len(sequence)):
        next_value = sequence[i]
        if current_value is next_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = next_value
            count = 1

    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_data = ['a', 'a', 'b', 'b', 'b', 'c', 'd', 'd', 'a', 'a', 'a']
    print(run_length_encode(sample_data))