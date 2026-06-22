def rle_compressed(text):
    if not text:
        return ""
    
    result = []
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]
        count = 1
        while i + count < n and text[i + count] == char:
            count += 1
        
        if count >= 3:
            result.append(f"{count}{char}")
            i += count
        else:
            for _ in range(count):
                result.append(char)
            i += count
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCCDDDE"
    compressed = rle_compressed(sample_input)
    print(compressed)