def rle_encode(s):
    if not s:
        return []
    
    chars = [c for c in s]
    encoded = []
    
    i = 0
    n = len(chars)
    
    while i < n:
        current_char = chars[i]
        count = 1
        while i + count < n and chars[i + count] == current_char:
            count += 1
        encoded.append((current_char, count))
        i += count
    
    return encoded

if __name__ == '__main__':
    sample_string = "aaabbcc"
    result = rle_encode(sample_string)
    print(result)