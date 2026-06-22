import itertools

def compress_repeated_chars(sequence):
    for char, group in itertools.groupby(sequence):
        count = sum((1 for _ in group))
        yield (char, count)

def reconstruct_sequence(encoded):
    return ''.join((char * count for char, count in encoded))
if __name__ == '__main__':
    original = 'zzzzzxyyy'
    encoded = list(compress_repeated_chars(original))
    reconstructed = reconstruct_sequence(encoded)
    print(encoded)
    print(reconstructed)
    print(original == reconstructed)