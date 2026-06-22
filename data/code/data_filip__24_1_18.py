def rle_decompress(compressed_string):
    decompressed = []
    i = 0
    while i < len(compressed_string):
        if compressed_string[i].isdigit():
            count = 0
            while i < len(compressed_string) and compressed_string[i].isdigit():
                count = count * 10 + int(compressed_string[i])
                i += 1
            char = compressed_string[i]
            decompressed.append(char * count)
            i += 1
        else:
            decompressed.append(compressed_string[i])
            i += 1
    return ''.join(decompressed)

if __name__ == '__main__':
    compressed = "3a1b2c"
    print(rle_decompress(compressed))
    compressed2 = "12A3B"
    print(rle_decompress(compressed2))
    compressed3 = "a1b2c3"
    print(rle_decompress(compressed3))
    compressed4 = "100x"
    print(rle_decompress(compressed4))
    compressed5 = ""
    print(rle_decompress(compressed5))