def rle_encode(text: str) -> list[tuple[str, int]]:
    if not text:
        return []
    
    encoded = []
    current_char = text[0]
    current_count = 1
    
    for char in text[1:]:
        if char == current_char:
            current_count += 1
        else:
            encoded.append((current_char, current_count))
            current_char = char
            current_count = 1
            
    encoded.append((current_char, current_count))
    return encoded

if __name__ == '__main__':
    sample_text = "AAABBC"
    result = rle_encode(sample_text)
    print(result)