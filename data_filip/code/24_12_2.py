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
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    
    return "".join(encoded)

if __name__ == '__main__':
    original_string = "AAABBBCCCC"
    compressed_string = run_length_encode(original_string)
    print(f"{original_string} -> {compressed_string}")