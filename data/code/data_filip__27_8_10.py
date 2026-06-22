def encode_rle(s):
    if not s:
        return []
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            encoded.append((count, current_char))
            current_char = char
            count = 1
    encoded.append((count, current_char))
    
    return encoded

if __name__ == '__main__':
    input_str = 'WWWWWWWWWWWWWBWWWWWWWWWWWWWWWBWWWWWWWWWWWWWWCCCCCCCCCC'
    result = encode_rle(input_str)
    print(result)