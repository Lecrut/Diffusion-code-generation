def rle_compress(text: str) -> str:
    if not text:
        return ""
    
    result = []
    i = 0
    length = len(text)
    
    while i < length:
        current_char = text[i]
        count = 1
        
        while i + count < length and text[i + count] == current_char:
            count += 1
        
        if count >= 3:
            result.append(f"{count}{current_char}")
        else:
            for _ in range(count):
                result.append(current_char)
        
        i += count
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCDA"
    output = rle_compress(sample_input)
    print(output)