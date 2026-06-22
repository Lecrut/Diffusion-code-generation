def decode_rle(encoded_list):
    decoded_parts = []
    for count, char in encoded_list:
        decoded_parts.append(char * count)
    return ''.join(decoded_parts)

if __name__ == '__main__':
    sample_encoded = [(3, 'a'), (2, 'b'), (5, 'c')]
    print(decode_rle(sample_encoded))