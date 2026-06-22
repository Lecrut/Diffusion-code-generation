def run_length_encode(text):
    if not text:
        return {}
    
    result = {}
    count = 0
    current_char = text[0]
    
    for char in text:
        if char == current_char:
            count += 1
        else:
            key = f"{count}{current_char}"
            result[key] = count
            current_char = char
            count = 1
    
    key = f"{count}{current_char}"
    result[key] = count
    return result

if __name__ == '__main__':
    sample_text = "aaabbccc"
    encoded = run_length_encode(sample_text)
    print(encoded)