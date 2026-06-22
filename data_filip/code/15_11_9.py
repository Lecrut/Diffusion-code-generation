def run_length_encode(text: str) -> str:
    if not text:
        return ''
    
    encoded_parts = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(str(count))
            encoded_parts.append(current_char)
            current_char = char
            count = 1
    
    encoded_parts.append(str(count))
    encoded_parts.append(current_char)
    
    return ''.join(encoded_parts)

if __name__ == '__main__':
    sample_string = "aaabbcccc"
    result = run_length_encode(sample_string)
    print(result)