from itertools import groupby

def run_length_encode(data):
    if not data:
        return []
    return [(len(list(group)), key) for key, group in groupby(data)]

def run_length_decode(encoded):
    result = []
    for count, value in encoded:
        result.extend([value] * count)
    return result

if __name__ == '__main__':
    sample_data = "AAABBBCCDAA"
    encoded = run_length_encode(sample_data)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(''.join(decoded))