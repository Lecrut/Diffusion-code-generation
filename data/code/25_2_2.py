def decode_rle(rle_list):
    result = []
    for char, count in rle_list:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    rle_data = [('a', 5), ('b', 2), ('c', 0), ('d', 3)]
    decoded_string = decode_rle(rle_data)
    print(decoded_string)