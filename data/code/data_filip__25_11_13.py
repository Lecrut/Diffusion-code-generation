def decompress_rle(encoded):
    if not encoded:
        return ""
    decoded_parts = []
    i = 0
    n = len(encoded)
    while i < n:
        num_str = ""
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
        else:
            break
    return "".join(decoded_parts)

if __name__ == "__main__":
    sample_encoded = "3A2B5C1A"
    result = decompress_rle(sample_encoded)
    print(result)