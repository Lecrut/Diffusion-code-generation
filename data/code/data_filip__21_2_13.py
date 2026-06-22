def run_length_encode(text: str) -> list:
    if not text:
        return []
    
    encoded_list = []
    current_char = text[0]
    current_count = 1
    
    for char in text[1:]:
        if char == current_char:
            current_count += 1
        else:
            encoded_list.append((current_char, current_count))
            current_char = char
            current_count = 1
            
    encoded_list.append((current_char, current_count))
    return encoded_list

if __name__ == '__main__':
    sample_text = "AAABBBCCCD"
    result = run_length_encode(sample_text)
    print(result)