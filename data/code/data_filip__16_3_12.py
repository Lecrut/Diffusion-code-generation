import itertools

def run_length_encode(chars):
    if not chars:
        return []
    result = []
    for key, group in itertools.groupby(chars):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample_chars = ['A', 'A', 'B', 'B', 'B', 'C', 'A', 'A', 'A']
    encoded = run_length_encode(sample_chars)
    print(encoded)

    sample_empty = []
    encoded_empty = run_length_encode(sample_empty)
    print(encoded_empty)

    sample_single = ['X']
    encoded_single = run_length_encode(sample_single)
    print(encoded_single)