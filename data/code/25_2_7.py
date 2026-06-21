def decode_rle(rle_data):
    result = []
    for char, count in rle_data:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_rle = [('a', 3), ('b', 1), ('c', 2)]
    decoded_string = decode_rle(sample_rle)
    print(decoded_string)