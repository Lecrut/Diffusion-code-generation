def decode_rle(encoded_list):
    result = []
    for char, count in encoded_list:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    rle_data = [('a', 3), ('b', 1), ('c', 4)]
    uncompressed = decode_rle(rle_data)
    print(uncompressed)