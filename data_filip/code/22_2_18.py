def decompress_rle(rle_string):
    decompressed = ''.join(
        char * int(count)
        for i, char in enumerate(rle_string)
        if i % 2 == 1
        for count in [int(rle_string[i - 1])]
    )
    return decompressed

if __name__ == '__main__':
    sample = "3a2b1c4d"
    print(decompress_rle(sample))