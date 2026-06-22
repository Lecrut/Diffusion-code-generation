def run_length_encode(chars):
    if not chars:
        return []
    
    encoded = []
    current_char = chars[0]
    count = 1
    
    for i in range(1, len(chars)):
        if chars[i] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = chars[i]
            count = 1
    
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_chars = ['A', 'A', 'B', 'B', 'B', 'C', 'A', 'A', 'A']
    result = run_length_encode(sample_chars)
    print(result)