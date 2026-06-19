def compute_length_ratio(lengths):
    min_len = min(lengths.values())
    max_len = max(lengths.values())
    ratio = max_len / min_len
    return ratio

if __name__ == '__main__':
    length_values = {'length1': 20, 'length2': 50}
    ratio = compute_length_ratio(length_values)
    print(ratio)