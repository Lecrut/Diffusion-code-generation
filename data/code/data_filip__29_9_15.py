def encode_repeated_elements(text):
    if not text:
        return ""
    
    encoded = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    result = encode_repeated_elements(sample_input)
    print(result)