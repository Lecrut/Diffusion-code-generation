import itertools

def run_length_encode(data):
    if not data:
        return []
    return [(key, len(list(group))) for key, group in itertools.groupby(data)]

if __name__ == '__main__':
    sample_input = "aaabbcccc"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    sample_numbers = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    encoded_numbers = run_length_encode(sample_numbers)
    print(encoded_numbers)