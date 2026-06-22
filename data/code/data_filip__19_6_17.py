def rle_encode_case_insensitive(text: str) -> str:
    if not text:
        return ""
    
    lower_text = text.lower()
    result = []
    count = 0
    current_char = lower_text[0]
    
    for char in lower_text:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample = "AaBbCcDDd"
    encoded = rle_encode_case_insensitive(sample)
    print(encoded)