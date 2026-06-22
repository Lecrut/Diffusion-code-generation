def rle_decompress(compressed_string):
    decompressed = []
    i = 0
    while i < len(compressed_string):
        if compressed_string[i].isdigit():
            count_str = ''
            while i < len(compressed_string) and compressed_string[i].isdigit():
                count_str += compressed_string[i]
                i += 1
            count = int(count_str)
            if i < len(compressed_string):
                char = compressed_string[i]
                decompressed.append(char * count)
                i += 1
            else:
                raise ValueError("Invalid RLE format: number at end of string without following character")
        else:
            decompressed.append(compressed_string[i])
            i += 1
    return ''.join(decompressed)

if __name__ == '__main__':
    compressed_samples = [
        'A3B2C1',
        'H2e4l3o1w2r4l2d2',
        '1A2B3C',
        'X5',
        'a1b1c1',
        '9Z',
        'A1',
        '12A3B',
        '',
        'Test11ing'
    ]
    for sample in compressed_samples:
        print(rle_decompress(sample))