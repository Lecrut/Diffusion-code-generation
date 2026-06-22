def rle_encode(text: str) -> str:
    if not text:
        return ""
    
    encoded = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    
    return "".join(encoded)

if __name__ == "__main__":
    result = rle_encode("aaabbc")
    print(result)
    
    result2 = rle_encode("")
    print(result2)
    
    result3 = rle_encode("abc")
    print(result3)