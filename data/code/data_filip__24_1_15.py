def decompress_rle(compressed: str) -> str:
    if not compressed:
        return ""
    
    result = []
    i = 0
    n = len(compressed)
    
    while i < n:
        char = compressed[i]
        if char.isdigit():
            count = int(char)
            i += 1
            if i < n and compressed[i].isdigit():
                count = count * 10 + int(compressed[i])
                i += 1
            next_char = compressed[i]
            result.append(next_char * count)
            i += 1
        else:
            result.append(char)
            i += 1
            
    return "".join(result)

if __name__ == '__main__':
    compressed_string = "a3b4c1d2"
    original_string = decompress_rle(compressed_string)
    print(original_string)