def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    if len(text) == 1:
        return text
    
    result = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = text[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_text = "AAABBBCCCA"
    encoded = run_length_encode(sample_text)
    print(encoded)