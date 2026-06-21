def decode_rle(encoded_list):
    result_parts = []
    for item in encoded_list:
        count, char = item
        result_parts.append(char * count)
    return ''.join(result_parts)

if __name__ == '__main__':
    sample_rle = [(3, 'a'), (2, 'b'), (1, 'c')]
    decoded_string = decode_rle(sample_rle)
    print(decoded_string)