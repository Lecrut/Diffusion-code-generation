def decode_rle(encoded_list):
    result = []
    for char, count in encoded_list:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_input = [('a', 3), ('b', 2), ('c', 5), ('d', 1)]
    output = decode_rle(sample_input)
    print(output)