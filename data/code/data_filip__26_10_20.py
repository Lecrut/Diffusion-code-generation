def rle_encode(s):
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    print(rle_encode("aabcccccaaa"))
    print(rle_encode("abc"))
    print(rle_encode("a"))
    print(rle_encode(""))
    print(rle_encode("aaabbbcc"))