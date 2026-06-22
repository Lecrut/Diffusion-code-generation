def compress_rle(text):
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    result.append(f"{current_char}{count}")
    
    compressed = "".join(result)
    
    if len(compressed) >= len(text):
        return text
    
    return compressed

if __name__ == '__main__':
    print(compress_rle("aaabbc"))
    print(compress_rle("abc"))
    print(compress_rle(""))
    print(compress_rle("aaaa"))
    print(compress_rle("abababababababababababababababababababababababab"))