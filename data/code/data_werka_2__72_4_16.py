def fetch_pair_at_index(source_a, source_b, position):
    if position < 0:
        raise ValueError("Index cannot be negative")
    if position >= len(source_a) or position >= len(source_b):
        raise ValueError("Index out of range for one or both lists")
    return [(source_a[position], source_b[position])]

if __name__ == '__main__':
    sample_list_one = [100, 200, 300]
    sample_list_two = [400, 500, 600]
    target_pos = 2
    computed_result = fetch_pair_at_index(sample_list_one, sample_list_two, target_pos)
    print(computed_result)