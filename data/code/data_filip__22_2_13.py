def decode_rle(s: str) -> str:
    result = []
    i = 0
    length = len(s)
    while i < length:
        char = s[i]
        i += 1
        if i < length and s[i].isdigit():
            num_str = ""
            while i < length and s[i].isdigit():
                num_str += s[i]
                i += 1
            count = int(num_str)
            result.append(char * count)
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    encoded = "a3b4c2d"
    decoded = decode_rle(encoded)
    print(decoded)