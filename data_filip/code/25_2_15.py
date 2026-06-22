def decode_rle(encoded_data):
    result = []
    for char, count in encoded_data:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_input = [('a', 3), ('b', 2), ('c', 1), ('d', 4)]
    decoded_string = decode_rle(sample_input)
    print(decoded_string)