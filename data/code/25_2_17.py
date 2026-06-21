def decode_rle(rle_list):
    if not rle_list:
        return ''
    result = []
    for char, count in rle_list:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    rle_input = [('a', 3), ('b', 2), ('c', 1)]
    decoded_string = decode_rle(rle_input)
    print(decoded_string)