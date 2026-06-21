from itertools import groupby

def run_length_encode(data):
    return [(k, len(list(g))) for k, g in groupby(data)]

def run_length_decode(encoded):
    return ''.join(k * n for k, n in encoded)

if __name__ == '__main__':
    sample = 'AAAABBBCCDAA'
    encoded = run_length_encode(sample)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)