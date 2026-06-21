def run_length_encode(sequence):
    if not sequence:
        return []
    result = []
    current_item = sequence[0]
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == current_item:
            count += 1
        else:
            result.append((current_item, count))
            current_item = sequence[i]
            count = 1
    result.append((current_item, count))
    return result

if __name__ == '__main__':
    sample_data = "AAABBBCCCCCDDDEE"
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)