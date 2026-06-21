from itertools import groupby

def run_length_encode(data):
    return [(key, sum((1 for _ in group))) for key, group in groupby(data)]
if __name__ == '__main__':
    sample_string = 'AAABBBCCDAA'
    encoded = run_length_encode(sample_string)
    print(encoded)
    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1]
    encoded_list = run_length_encode(sample_list)
    print(encoded_list)
    empty_sample = ''
    encoded_empty = run_length_encode(empty_sample)
    print(encoded_empty)
    single_sample = 'A'
    encoded_single = run_length_encode(single_sample)
    print(encoded_single)
    mixed_sample = 'aabbbccccddee'
    encoded_mixed = run_length_encode(mixed_sample)
    print(encoded_mixed)