def rle_compress(text: str) -> str:
    if not text:
        return ""
    
    compressed = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    compressed.append(f"{count}{current_char}")
    
    return "".join(compressed)

if __name__ == '__main__':
    sample_string = "AAABBBCCC"
    result = rle_compress(sample_string)
    print(result)