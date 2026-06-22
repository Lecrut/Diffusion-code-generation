import itertools

def run_length_encode(input_string):
    if not input_string:
        return []
    result = []
    for key, group in itertools.groupby(input_string):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample_data = "aaabbccccddee"
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)