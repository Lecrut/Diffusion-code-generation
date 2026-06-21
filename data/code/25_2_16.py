def decode_rle(encoded):
    result = []
    for char, count in encoded:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_encoded = [('a', 3), ('b', 2), ('c', 5)]
    print(decode_rle(sample_encoded))