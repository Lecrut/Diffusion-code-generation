def decode_rle(encoded_list):
    result = []
    for count, char in encoded_list:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_data = [(4, 'a'), (2, 'b'), (3, 'c')]
    print(decode_rle(sample_data))