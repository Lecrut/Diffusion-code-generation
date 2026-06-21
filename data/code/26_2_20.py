def run_length_encode(text: str) -> list:
    if not text:
        return []
    
    encoded = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
            
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    samples = ["AABBCCCD", "", "AAABBBCCC", "A"]
    for sample in samples:
        print(run_length_encode(sample))