def rle_encode_case_insensitive(text):
    if not text:
        return ""
    
    text = text.lower()
    if len(text) == 1:
        return "1a"
    
    result = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = text[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_text = "AaaBBcc"
    encoded = rle_encode_case_insensitive(sample_text)
    print(encoded)