def rle_encode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample1 = "WWWWWWWWWWWWBWWWW"
    sample2 = "ABBC"
    sample3 = "A"
    sample4 = ""
    sample5 = "AAABBBCCC"
    
    print(rle_encode(sample1))
    print(rle_encode(sample2))
    print(rle_encode(sample3))
    print(rle_encode(sample4))
    print(rle_encode(sample5))