def decode_rle(s):
    if not s:
        return ""
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        if s[i].isdigit():
            j = i
            while j < n and s[j].isdigit():
                j += 1
            count = int(s[i:j])
            if j >= n:
                raise ValueError("RLE string ends with digits but no character follows")
            char = s[j]
            if not char.isalpha():
                raise ValueError(f"Invalid character '{char}' in RLE decoding")
            result.append(char * count)
            i = j + 1
        elif s[i].isalpha():
            result.append(s[i])
            i += 1
        else:
            raise ValueError(f"Invalid character '{s[i]}' in RLE string")
    
    return "".join(result)

if __name__ == '__main__':
    encoded_string = "3A4B2C"
    decoded = decode_rle(encoded_string)
    print(decoded)