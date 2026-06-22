def decompress_rle(encoded: str) -> str:
    result = []
    i = 0
    n = len(encoded)
    while i < n:
        if encoded[i].isdigit():
            start = i
            while i < n and encoded[i].isdigit():
                i += 1
            count = int(encoded[start:i])
        else:
            char = encoded[i]
            count = 1
            i += 1
        if count > 1:
            result.append(char * count)
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    encoded_input = "a3b2c4"
    output = decompress_rle(encoded_input)
    print(output)