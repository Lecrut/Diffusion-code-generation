def decode_rle(rle_data):
    result = []
    for char, count in rle_data:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_rle = [('a', 3), ('b', 2), ('c', 5)]
    decoded = decode_rle(sample_rle)
    print(decoded)