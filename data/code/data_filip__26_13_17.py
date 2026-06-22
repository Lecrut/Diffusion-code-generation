def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    encoded_chars = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded_chars.append(f"{count}{current_char}")
            current_char = text[i]
            count = 1
    
    encoded_chars.append(f"{count}{current_char}")
    
    return "".join(encoded_chars)

if __name__ == "__main__":
    sample_string = "AAAABBBCCDAA"
    result = run_length_encode(sample_string)
    print(result)