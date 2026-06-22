def rle_encode_case_insensitive(text):
    if not text:
        return ""
    
    lower_text = text.lower()
    result = []
    current_char = lower_text[0]
    count = 1
    
    for i in range(1, len(lower_text)):
        char = lower_text[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_text = "AaaaBBBcc"
    encoded = rle_encode_case_insensitive(sample_text)
    print(encoded)