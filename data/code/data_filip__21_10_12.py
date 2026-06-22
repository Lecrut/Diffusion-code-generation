from itertools import groupby

def run_length_encode(data):
    if not data:
        return []
    result = []
    for key, group in groupby(data):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample_input = "aaabbccccd"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)