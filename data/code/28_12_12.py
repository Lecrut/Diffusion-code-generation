def run_length_compress(data):
    if not data:
        return []

    compressed = []
    current_char = data[0]
    count = 1

    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = data[i]
            count = 1

    compressed.append((current_char, count))
    return compressed

if __name__ == '__main__':
    sample_data = ['A', 'A', 'A', 'B', 'B', 'A', 'C', 'C', 'C', 'C']
    result = run_length_compress(sample_data)
    print(result)

    sample_data_empty = []
    result_empty = run_length_compress(sample_data_empty)
    print(result_empty)

    sample_data_single = ['X']
    result_single = run_length_compress(sample_data_single)
    print(result_single)

    sample_data_alternating = ['A', 'B', 'A', 'B']
    result_alternating = run_length_compress(sample_data_alternating)
    print(result_alternating)