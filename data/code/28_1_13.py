def decode_rle(rle_list):
    decoded_parts = []
    for char, count in rle_list:
        decoded_parts.append(char * count)
    return ''.join(decoded_parts)
if __name__ == '__main__':
    rle_encoded = [('a', 5), ('b', 2), ('c', 3)]
    result = decode_rle(rle_encoded)
    print(result)