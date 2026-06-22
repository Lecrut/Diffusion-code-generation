def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    result: list[str] = []
    current_char: str = text[0]
    count: int = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_text: str = "aabcccccaaa"
    encoded_result: str = run_length_encode(sample_text)
    print(encoded_result)