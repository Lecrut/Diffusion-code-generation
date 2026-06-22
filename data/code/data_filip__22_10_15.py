def compress_rle(s):
    if not s:
        return ""
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        char = s[i]
        count = 1
        while i + 1 < n and s[i + 1] == char:
            count += 1
            i += 1
        result.append(f"{char}{count}")
        i += 1
    
    compressed = "".join(result)
    return compressed if len(compressed) < len(s) else s

if __name__ == '__main__':
    print(compress_rle("aabcccccaaa"))
    print(compress_rle("abcde"))
    print(compress_rle(""))
    print(compress_rle("aaaa"))