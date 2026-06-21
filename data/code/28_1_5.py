def decode_rle(rle_list):
    decoded = []
    iterator = iter(rle_list)
    for count in iterator:
        character = next(iterator)
        decoded.append(character * count)
    return ''.join(decoded)

if __name__ == '__main__':
    sample_rle = [2, 'a', 3, 'b', 1, 'c']
    result = decode_rle(sample_rle)
    print(result)