def run_length_encode(data):
    if not data:
        return {}
    counts = {}
    current = data[0]
    count = 1
    for item in data[1:]:
        if item == current:
            count += 1
        else:
            counts[current] = counts.get(current, 0) + count
            current = item
            count = 1
    counts[current] = counts.get(current, 0) + count
    return counts

if __name__ == '__main__':
    sample_list = [1, 1, 2, 2, 2, 3, 4, 4]
    result = run_length_encode(sample_list)
    print(result)

    sample_string = "aaabbcdd"
    result_string = run_length_encode(sample_string)
    print(result_string)

    empty_list = []
    result_empty = run_length_encode(empty_list)
    print(result_empty)

    single_item = [5]
    result_single = run_length_encode(single_item)
    print(result_single)

    mixed_types = [1, 'a', 'a', 2]
    result_mixed = run_length_encode(mixed_types)
    print(result_mixed)