def decode_rle(encoded):
    result = []
    for char, count in encoded:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_encoded = [('a', 3), ('b', 2), ('c', 1), ('d', 5)]
    decoded_string = decode_rle(sample_encoded)
    print(decoded_string)

    sample_encoded2 = [('x', 0), ('y', 1), ('z', 3)]
    decoded_string2 = decode_rle(sample_encoded2)
    print(decoded_string2)

    sample_encoded3 = [('A', 5)]
    decoded_string3 = decode_rle(sample_encoded3)
    print(decoded_string3)

    sample_encoded4 = []
    decoded_string4 = decode_rle(sample_encoded4)
    print(decoded_string4)

    sample_encoded5 = [(' ', 3), ('!', 2)]
    decoded_string5 = decode_rle(sample_encoded5)
    print(decoded_string5)