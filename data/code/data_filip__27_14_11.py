def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 3:
                result.append(f"{count}{current_char}")
            elif count > 1:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char)
            current_char = char
            count = 1
    
    if count > 3:
        result.append(f"{count}{current_char}")
    elif count > 1:
        result.append(f"{count}{current_char}")
    else:
        result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    text = "AAABBBCCD"
    encoded = run_length_encode(text)
    print(encoded)
    
    text2 = "A"
    encoded2 = run_length_encode(text2)
    print(encoded2)
    
    text3 = "AABCAADDD"
    encoded3 = run_length_encode(text3)
    print(encoded3)