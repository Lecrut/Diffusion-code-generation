def run_length_encode(text):
    if not text:
        return ""
    
    encoded_chars = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            encoded_chars.append(current_char)
            encoded_chars.append(str(count))
            current_char = char
            count = 1
            
    encoded_chars.append(current_char)
    encoded_chars.append(str(count))
    
    return "".join(encoded_chars)

if __name__ == '__main__':
    sample_input = "AAAABBBCCDAA"
    result = run_length_encode(sample_input)
    print(result)