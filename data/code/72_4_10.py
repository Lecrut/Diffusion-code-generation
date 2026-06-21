def fetch_pair_from_lists(first_sequence, second_sequence, position):
    if position < 0:
        raise ValueError("Position must be non-negative")
    if position >= len(first_sequence):
        raise ValueError("Position out of range for first sequence")
    if position >= len(second_sequence):
        raise ValueError("Position out of range for second sequence")
    left_value = first_sequence[position]
    right_value = second_sequence[position]
    return [(left_value, right_value)]

if __name__ == '__main__':
    data_one = [100, 200, 300]
    data_two = [400, 500, 600]
    target = 1
    answer = fetch_pair_from_lists(data_one, data_two, target)
    print(answer)