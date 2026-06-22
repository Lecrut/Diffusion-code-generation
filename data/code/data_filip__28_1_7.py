def decode_rle(encoded):
    decoded_chars = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        count = encoded[i + 1]
        decoded_chars.append(char * count)
        i += 2
    return ''.join(decoded_chars)

if __name__ == '__main__':
    sample_encoded = [('a', 3), ('b', 2), ('c', 5)]
    print(decode_rle(sample_encoded))