def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    result: list[str] = []
    current_char: str = text[0]
    count: int = 1
    
    for i in range(1, len(text)):
        char: str = text[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_input: str = "AAABBBCCDAA"
    encoded_output: str = run_length_encode(sample_input)
    print(encoded_output)