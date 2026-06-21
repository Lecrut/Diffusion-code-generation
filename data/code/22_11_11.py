def decode_rle(encoded: str) -> str:
    result = []
    i = 0
    length = len(encoded)
    while i < length:
        char = encoded[i]
        i += 1
        count_str = ""
        while i < length and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        if count_str:
            count = int(count_str)
            result.append(char * count)
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample_encoded = "a3b4c2d1"
    decoded_string = decode_rle(sample_encoded)
    print(decoded_string)