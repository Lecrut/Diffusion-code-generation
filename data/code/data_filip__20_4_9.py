def run_length_encode(text):
    if not text:
        return ""
    
    encoded_parts = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{count}{current_char}")
            current_char = char
            count = 1
            
    encoded_parts.append(f"{count}{current_char}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_text = "aaabbc"
    result = run_length_encode(sample_text)
    print(result)