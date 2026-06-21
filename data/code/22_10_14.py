def compress_rle(s):
    if not s:
        return ""
    
    compressed = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = s[i]
            count = 1
    
    compressed.append(current_char)
    compressed.append(str(count))
    
    return "".join(compressed)

if __name__ == '__main__':
    print(compress_rle("aabcccccaaa"))
    print(compress_rle("abc"))
    print(compress_rle("a"))
    print(compress_rle(""))
    print(compress_rle("aaaabbbbccccddd"))
    print(compress_rle("xyzzzxy"))