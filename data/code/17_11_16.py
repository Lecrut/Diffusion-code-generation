def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    encoded_parts: list[str] = []
    current_char: str = input_string[0]
    count: int = 1
    index: int = 1
    length: int = len(input_string)
    
    while index < length:
        char: str = input_string[index]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded_parts.append(f"{count}{current_char}")
            else:
                encoded_parts.append(current_char)
            current_char = char
            count = 1
        index += 1
    
    if count > 1:
        encoded_parts.append(f"{count}{current_char}")
    else:
        encoded_parts.append(current_char)
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_text: str = "AAAAABBBCCDEEEE"
    result: str = run_length_encode(sample_text)
    print(result)