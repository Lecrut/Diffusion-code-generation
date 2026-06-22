def decode_rle(rle_data):
    result = []
    for char, count in rle_data:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    rle_list = [('a', 5), ('b', 3), ('c', 1)]
    decoded_string = decode_rle(rle_list)
    print(decoded_string)