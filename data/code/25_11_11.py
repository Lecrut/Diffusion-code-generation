def decompress_rle(encoded: str) -> str:
    decoded_chars = []
    i = 0
    n = len(encoded)
    while i < n:
        count_str = ""
        while i < n and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        count = int(count_str) if count_str else 1
        if i < n:
            char = encoded[i]
            decoded_chars.append(char * count)
            i += 1
    return "".join(decoded_chars)

if __name__ == '__main__':
    sample_encoded = "3a2b4c"
    result = decompress_rle(sample_encoded)
    print(result)

    sample_encoded2 = "12w3z"
    result2 = decompress_rle(sample_encoded2)
    print(result2)

    sample_encoded3 = "1a1b1c"
    result3 = decompress_rle(sample_encoded3)
    print(result3)