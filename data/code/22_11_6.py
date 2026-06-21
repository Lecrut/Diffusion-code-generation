def decompress_rle(encoded: str) -> str:
    decompressed = []
    i = 0
    while i < len(encoded):
        if not encoded[i].isdigit():
            char = encoded[i]
            i += 1
            count_str = ''
            while i < len(encoded) and encoded[i].isdigit():
                count_str += encoded[i]
                i += 1
            count = int(count_str) if count_str else 1
            decompressed.append(char * count)
        else:
            raise ValueError(f"Invalid RLE format: digit '{encoded[i]}' found where character expected at position {i}")
    return ''.join(decompressed)
if __name__ == '__main__':
    sample1 = 'a3b2c1'
    result1 = decompress_rle(sample1)
    print(result1)
    sample2 = 'A5B2C10'
    result2 = decompress_rle(sample2)
    print(result2)
    sample3 = 'z1a1'
    result3 = decompress_rle(sample3)
    print(result3)
    sample4 = ''
    result4 = decompress_rle(sample4)
    print(result4)