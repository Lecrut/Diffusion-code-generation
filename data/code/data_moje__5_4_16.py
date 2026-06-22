def compare_length_lists(list_a, list_b):
    if not list_a or not list_b:
        raise ValueError("Lists must not be empty")

    all_lengths = list_a + list_b
    max_length = max(all_lengths)
    min_length = min(all_lengths)
    range_difference = max_length - min_length

    return {
        'max_length': max_length,
        'min_length': min_length,
        'range_difference': range_difference
    }

if __name__ == '__main__':
    list_a = [10.5, 20.3, 15.0]
    list_b = [12.1, 8.4, 25.6]

    result = compare_length_lists(list_a, list_b)

    print(result)