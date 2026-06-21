def decompress_rle(encoded: str) -> str:
    if not encoded:
        return ''

    decoded_parts = []
    i = 0
    n = len(encoded)

    while i < n:
        num_str = ''
        while i < n and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1

        if not num_str:
            count = 1
        else:
            count = int(num_str)

        if i < n:
            char = encoded[i]
            i += 1
            decoded_parts.append(char * count)

    return ''.join(decoded_parts)

if __name__ == '__main__':
    sample_encoded = '2a3b4c'
    print(decompress_rle(sample_encoded))

    sample_encoded2 = '10A'
    print(decompress_rle(sample_encoded2))

    sample_encoded3 = ''
    print(decompress_rle(sample_encoded3))

    sample_encoded4 = '1x'
    print(decompress_rle(sample_encoded4))