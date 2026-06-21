import itertools

def run_length_encoding(input_string):
    if not input_string:
        return []
    result = []
    for key, group in itertools.groupby(input_string):
        length = sum(1 for _ in group)
        result.append((key, length))
    return result

if __name__ == '__main__':
    sample_data = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_result = run_length_encoding(sample_data)
    print(encoded_result)