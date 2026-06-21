from itertools import groupby

def run_length_encode(data):
    return tuple((key, len(list(group))) for key, group in groupby(data))

if __name__ == '__main__':
    sample_data = "AAABBBCCDAA"
    result = run_length_encode(sample_data)
    print(result)

    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    result_list = run_length_encode(sample_list)
    print(result_list)

    mixed_data = [1, "a", "a", 2, 2, 2, None, None]
    result_mixed = run_length_encode(mixed_data)
    print(result_mixed)