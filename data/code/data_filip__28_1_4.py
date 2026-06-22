def decode_rle(encoded):
    decoded = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        count = encoded[i + 1]
        decoded.append(char * count)
        i += 2
    return ''.join(decoded)

if __name__ == '__main__':
    sample_encoded = [('a', 3), ('b', 1), ('c', 2)]
    print(decode_rle(sample_encoded))