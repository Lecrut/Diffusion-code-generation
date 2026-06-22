def rle_compress_mod(text: str) -> str:
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    length = len(text)
    
    for i in range(1, length):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            if count >= 3:
                result.append(f"{count}{current_char}")
            else:
                for _ in range(count):
                    result.append(current_char)
            current_char = char
            count = 1
    
    if count >= 3:
        result.append(f"{count}{current_char}")
    else:
        for _ in range(count):
            result.append(current_char)
            
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbccdddddeffg"
    compressed = rle_compress_mod(sample_text)
    print(compressed)