def run_length_encode(text: str):
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        result.append(f"{count}{current_char}")
    else:
        result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)