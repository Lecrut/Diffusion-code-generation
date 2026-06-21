def decode_rle(encoded_list):
    result = []
    for char, count in encoded_list:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_data = [('a', 3), ('b', 2), ('c', 4), ('d', 1)]
    print(decode_rle(sample_data))