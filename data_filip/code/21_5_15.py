def run_length_encode(text: str) -> list[tuple]:
    if not text:
        return []
    
    encoded = []
    count = 1
    prev_char = text[0]
    
    for current_char in text[1:]:
        if current_char == prev_char:
            count += 1
        else:
            encoded.append((prev_char, count))
            prev_char = current_char
            count = 1
    
    encoded.append((prev_char, count))
    return encoded

if __name__ == '__main__':
    result = run_length_encode("aaabbc")
    print(result)