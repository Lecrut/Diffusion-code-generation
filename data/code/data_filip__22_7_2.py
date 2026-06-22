def rle_decode(s: str) -> str:
    if not s:
        return ""
    result = []
    i = 0
    n = len(s)
    while i < n:
        count = 0
        while i < n and s[i].isdigit():
            count = count * 10 + int(s[i])
            i += 1
        if i < n:
            char = s[i]
            i += 1
            if count > 0:
                result.append(char * count)
            else:
                result.append(char)
    return "".join(result)

if __name__ == '__main__':
    compressed_input = "a3b2c4"
    decoded_output = rle_decode(compressed_input)
    print(decoded_output)