def decode_rle(encoded_list):
    result = []
    for value, count in encoded_list:
        result.append(value * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_data = [('a', 3), ('b', 2), ('c', 1), ('d', 4)]
    decoded_string = decode_rle(sample_data)
    print(decoded_string)