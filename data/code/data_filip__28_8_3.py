def compress_run_length(int_list):
    if not int_list:
        return []

    result = []
    current_value = int_list[0]
    count = 1

    for item in int_list[1:]:
        if item == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = item
            count = 1

    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 1, 1]
    compressed = compress_run_length(sample_data)
    print(compressed)

    empty_data = []
    compressed_empty = compress_run_length(empty_data)
    print(compressed_empty)

    single_item = [42]
    compressed_single = compress_run_length(single_item)
    print(compressed_single)

    large_runs = [7] * 1000 + [8] * 500
    compressed_large = compress_run_length(large_runs)
    print(compressed_large)