def run_length_encode(sequence):
    if not sequence:
        return []
    result = []
    current_value = sequence[0]
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == current_value:
            count += 1
        else:
            result.append((count, current_value))
            current_value = sequence[i]
            count = 1
    result.append((count, current_value))
    return result

if __name__ == '__main__':
    sample = ['A', 'A', 'B', 'B', 'B', 'C', 'A']
    print(run_length_encode(sample))