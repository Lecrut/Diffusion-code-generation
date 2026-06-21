def run_length_encode(text):
    if not text:
        return []
    
    result = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)