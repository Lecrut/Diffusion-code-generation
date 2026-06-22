def decode_rle(encoded):
    result = []
    for char, count in encoded:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_encoded = [('a', 3), ('b', 2), ('c', 5)]
    decoded_string = decode_rle(sample_encoded)
    print(decoded_string)
    
    another_sample = [('x', 1), ('y', 10), ('z', 0)]
    another_decoded = decode_rle(another_sample)
    print(another_decoded)
    
    edge_case = []
    edge_decoded = decode_rle(edge_case)
    print(repr(edge_decoded))
    
    single_char = [('A', 1)]
    single_decoded = decode_rle(single_char)
    print(single_decoded)