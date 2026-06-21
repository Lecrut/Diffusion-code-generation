def decompress_rle(encoded: str) -> str:
    if not encoded:
        return ""

    result = []
    i = 0
    while i < len(encoded):
        if not encoded[i].isdigit():
            char = encoded[i]
            i += 1
            count_str = ""
            while i < len(encoded) and encoded[i].isdigit():
                count_str += encoded[i]
                i += 1
            count = int(count_str) if count_str else 1
            result.append(char * count)
        else:
            i += 1

    return "".join(result)

if __name__ == '__main__':
    sample_encoded = "a3b2c1"
    print(decompress_rle(sample_encoded))

    sample_encoded_multi = "x21y2"
    print(decompress_rle(sample_encoded_multi))

    sample_encoded_empty = ""
    print(decompress_rle(sample_encoded_empty))

    sample_encoded_single = "z1"
    print(decompress_rle(sample_encoded_single))

    sample_encoded_complex = "A1B2C3D4"
    print(decompress_rle(sample_encoded_complex))