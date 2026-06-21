def compress_run_length(data):
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = data[i]
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_input = ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'C', 'A']
    compressed = compress_run_length(sample_input)
    print(compressed)