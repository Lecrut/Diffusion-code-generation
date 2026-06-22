def rle_compress_tweaked(text: str) -> str:
    if not text:
        return ""
    
    result = []
    i = 0
    n = len(text)
    
    while i < n:
        current_char = text[i]
        count = 1
        
        while i + count < n and text[i + count] == current_char:
            count += 1
        
        if count >= 3:
            result.append(f"{count}{current_char}")
        else:
            for k in range(count):
                result.append(current_char)
        
        i += count
    
    return "".join(result)

if __name__ == '__main__':
    print(rle_compress_tweaked("aaabbccaaabb"))