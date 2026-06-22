def run_length_encode(text: str) -> dict:
    if not text:
        return {}
    
    result = {}
    count = 0
    current_char = text[0]
    
    for char in text:
        if char == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = char
            count = 1
    result[current_char] = count
    return result

if __name__ == '__main__':
    sample_text = "aaabbc"
    encoded = run_length_encode(sample_text)
    print(encoded)