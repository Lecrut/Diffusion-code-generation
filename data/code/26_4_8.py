def run_length_encode(text):
    if not text:
        return ""
    
    result = []
    count = 1
    current_char = text[0]
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                yield f"{count}{current_char}"
            else:
                yield current_char
            current_char = char
            count = 1
    
    if count > 1:
        yield f"{count}{current_char}"
    else:
        yield current_char

def encode_string(text):
    return "".join(run_length_encode(text))

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    encoded_result = encode_string(sample_input)
    print(encoded_result)