def decompress_rle(s: str) -> str:
    result = []
    count = 0
    for char in s:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            if count > 0:
                result.append(char * count)
                count = 0
            else:
                result.append(char)
    if count > 0:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    encoded_string = "a3b2c4"
    decoded_string = decompress_rle(encoded_string)
    print(decoded_string)