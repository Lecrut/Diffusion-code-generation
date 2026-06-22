import itertools

def run_length_encode(data):
    if not data:
        return tuple()
    grouped = itertools.groupby(data)
    result = tuple((key, sum(1 for _ in group)) for key, group in grouped)
    return result

if __name__ == '__main__':
    sample_data = "AAABBBCCDAA"
    encoded = run_length_encode(sample_data)
    print(encoded)

    sample_data_int = [1, 1, 2, 2, 2, 3, 4, 4]
    encoded_int = run_length_encode(sample_data_int)
    print(encoded_int)

    empty_data = ""
    encoded_empty = run_length_encode(empty_data)
    print(encoded_empty)