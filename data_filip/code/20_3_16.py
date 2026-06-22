def rle_encode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    count = 1
    current_char = text[0]
    
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

def rle_decode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    i = 0
    
    while i < len(text):
        count_str = []
        while i < len(text) and text[i].isdigit():
            count_str.append(text[i])
            i += 1
        
        count = int("".join(count_str))
        
        if i < len(text):
            char = text[i]
            i += 1
            result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBBCCCAAA"
    encoded = rle_encode(original)
    decoded = rle_decode(encoded)
    print(encoded)
    print(decoded)