def decode_rle(encoded_list):
    result = []
    for count, char in encoded_list:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_data = [(4, 'A'), (3, 'B'), (2, 'C'), (5, 'D')]
    print(decode_rle(sample_data))