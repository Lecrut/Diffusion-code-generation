def decode_rle(encoded):
    decoded = []
    for char, count in encoded:
        decoded.append(char * count)
    return ''.join(decoded)

if __name__ == '__main__':
    sample_encoded = [('A', 3), ('B', 2), ('C', 1)]
    print(decode_rle(sample_encoded))
    sample_encoded2 = [('x', 5), ('y', 0), ('z', 3)]
    print(decode_rle(sample_encoded2))
    sample_encoded3 = []
    print(decode_rle(sample_encoded3))