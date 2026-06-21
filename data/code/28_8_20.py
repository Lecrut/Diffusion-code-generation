def compress_run_length(data):
    if not data:
        return []

    result = []
    current_value = data[0]
    count = 1

    for item in data[1:]:
        if item == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = item
            count = 1

    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5]
    compressed = compress_run_length(sample_data)
    print(compressed)

    empty_data = []
    compressed_empty = compress_run_length(empty_data)
    print(compressed_empty)

    single_element = [42]
    compressed_single = compress_run_length(single_element)
    print(compressed_single)

    large_repeated = [7] * 1000000
    compressed_large = compress_run_length(large_repeated)
    print(compressed_large)

    alternating = [1, 2, 1, 2, 1, 2]
    compressed_alternating = compress_run_length(alternating)
    print(compressed_alternating)