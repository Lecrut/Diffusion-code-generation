from itertools import groupby

def run_length_encode(input_string):
    if not input_string:
        return []
    result = []
    for char, group in groupby(input_string):
        length = len(list(group))
        result.append((char, length))
    return result

if __name__ == '__main__':
    sample_input = "aaabbccc"
    encoded = run_length_encode(sample_input)
    print(encoded)