def decode_rle(rle_list):
    result = []
    for char, count in rle_list:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    rle_data = [('a', 4), ('b', 2), ('c', 1), ('d', 5)]
    compressed_str = decode_rle(rle_data)
    print(compressed_str)