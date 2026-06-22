def run_length_encode(sequence):
    if not sequence:
        return {}
    result = {}
    current_char = sequence[0]
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = sequence[i]
            count = 1
    result[current_char] = count
    return result

if __name__ == '__main__':
    sample_sequence = "aaabbbccdaa"
    print(run_length_encode(sample_sequence))