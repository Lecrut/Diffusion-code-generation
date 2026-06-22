def decode_rle(rle_list):
    decoded = []
    iterator = iter(rle_list)
    for count in iterator:
        char = next(iterator)
        decoded.append(char * count)
    return ''.join(decoded)

if __name__ == '__main__':
    sample_rle = [2, 'a', 1, 'b', 3, 'c']
    result = decode_rle(sample_rle)
    print(result)