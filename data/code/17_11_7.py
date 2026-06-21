def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    encoded_chars: list[str] = []
    current_char: str = text[0]
    count: int = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_chars.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded_chars.append(f"{count}{current_char}")
    
    return "".join(encoded_chars)

if __name__ == '__main__':
    sample_string: str = "AAAABBBCCDAA"
    result: str = run_length_encode(sample_string)
    print(result)