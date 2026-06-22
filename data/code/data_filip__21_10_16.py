from itertools import groupby

def run_length_encode(data):
    if not data:
        return []
    encoded = []
    for key, group in groupby(data):
        count = sum(1 for _ in group)
        encoded.append((key, count))
    return encoded

def run_length_decode(encoded):
    decoded = []
    for value, count in encoded:
        decoded.extend([value] * count)
    return decoded

if __name__ == '__main__':
    sample_data = "AAABBBCCCDAA"
    encoded = run_length_encode(sample_data)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)