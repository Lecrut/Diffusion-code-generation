def run_length_encode(text: str) -> str:
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
    original_string = "aaabbc"
    compressed = run_length_encode(original_string)
    print(compressed)