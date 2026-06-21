def decode_rle(encoded_list):
    result = []
    for pair in encoded_list:
        count, char = pair
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_encoded = [(3, 'A'), (2, 'B'), (4, 'C'), (1, 'D')]
    print(decode_rle(sample_encoded))