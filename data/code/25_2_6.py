def decode_rle(encoded):
    return ''.join(char * count for char, count in encoded)

if __name__ == '__main__':
    encoded_data = [('a', 3), ('b', 1), ('c', 2)]
    decoded_string = decode_rle(encoded_data)
    print(decoded_string)