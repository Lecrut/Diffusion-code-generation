def decompress_rle(encoded_string: str) -> str:
    if not encoded_string:
        return ""
    
    result = []
    i = 0
    length = len(encoded_string)
    
    while i < length:
        char = encoded_string[i]
        i += 1
        
        if i < length and encoded_string[i].isdigit():
            count_chars = []
            while i < length and encoded_string[i].isdigit():
                count_chars.append(encoded_string[i])
                i += 1
            count = int("".join(count_chars))
            result.append(char * count)
        else:
            result.append(char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "a3b2c10d1"
    output = decompress_rle(sample_input)
    print(output)