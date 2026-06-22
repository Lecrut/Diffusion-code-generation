import itertools

def run_length_encode(data):
    return [(c, len(list(group))) for c, group in itertools.groupby(data)]

def run_length_decode(encoded):
    return ''.join(char * count for char, count in encoded)

if __name__ == '__main__':
    sample = "AAAABBBCCDAA"
    encoded = run_length_encode(sample)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)