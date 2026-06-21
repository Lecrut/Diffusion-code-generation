def rle_encode(s):
    if not s:
        return ""
    
    encoded = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    print(rle_encode(""))
    print(rle_encode("a"))
    print(rle_encode("aa"))
    print(rle_encode("aabbc"))
    print(rle_encode("aaaabbbbcccd"))
    print(rle_encode("xyzzz"))
    print(rle_encode("111223333"))