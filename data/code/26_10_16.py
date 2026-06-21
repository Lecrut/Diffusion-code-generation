def rle_encode(s):
    if not s:
        return ''
    
    encoded_parts = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded_parts.append(str(count) + current_char)
            current_char = s[i]
            count = 1
            
    encoded_parts.append(str(count) + current_char)
    return ''.join(encoded_parts)

if __name__ == '__main__':
    print(rle_encode('AABBBCCCC'))
    print(rle_encode('ABC'))
    print(rle_encode(''))
    print(rle_encode('AAAAA'))
    print(rle_encode('A'))
    print(rle_encode('AABBCC'))