def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    encoded = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    
    encoded.append(str(count) + current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_text = "AAABBBCCCA"
    result = run_length_encode(sample_text)
    print(result)