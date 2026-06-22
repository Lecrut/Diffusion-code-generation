def decode_rle(encoded_data):
    decoded_parts = []
    for char, count in encoded_data:
        decoded_parts.append(char * count)
    return ''.join(decoded_parts)

if __name__ == '__main__':
    sample_rle = [('a', 3), ('b', 1), ('c', 2)]
    result = decode_rle(sample_rle)
    print(result)