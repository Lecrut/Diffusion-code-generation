def rle_encode(s):
    if not s:
        return ""
    
    encoded_parts = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded_parts.append(str(count))
            encoded_parts.append(current_char)
            current_char = s[i]
            count = 1
            
    if count > 1:
        encoded_parts.append(str(count))
    encoded_parts.append(current_char)
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    print(rle_encode("aabcccccaaa"))
    print(rle_encode("abcdef"))
    print(rle_encode("AAABBBCCCD"))
    print(rle_encode(""))
    print(rle_encode("A"))