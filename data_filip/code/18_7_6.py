def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    if len(text) == 1:
        return f"1{text[0]}"
    
    encoded = []
    current_char = text[0]
    count = 1
    length = len(text)
    
    for i in range(1, length):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCCCDDDDD"
    result = run_length_encode(sample_string)
    print(result)