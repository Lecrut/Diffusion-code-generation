from itertools import groupby

def run_length_encode(sequence):
    return [(char, len(list(group))) for char, group in groupby(sequence)]

def run_length_decode(encoded_sequence):
    return ''.join(char * count for char, count in encoded_sequence)

if __name__ == '__main__':
    original = "aabbbcccc"
    encoded = run_length_encode(original)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)