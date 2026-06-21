def run_length_encode(text: str) -> list:
    if not text:
        return []
    
    result = []
    current_char = text[0]
    current_count = 1
    
    for char in text[1:]:
        if char == current_char:
            current_count += 1
        else:
            result.append((current_char, current_count))
            current_char = char
            current_count = 1
    
    result.append((current_char, current_count))
    return result

if __name__ == '__main__':
    print(run_length_encode("AAABBBCC"))