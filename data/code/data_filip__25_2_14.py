def decode_rle(encoded_data):
    decoded = []
    for char, count in encoded_data:
        decoded.append(char * count)
    return ''.join(decoded)

if __name__ == '__main__':
    sample_encoded = [('H', 1), ('e', 1), ('l', 3), ('o', 2)]
    result = decode_rle(sample_encoded)
    print(result)