def rle_encode(text):
    if not text:
        return
    
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            yield f"{count}{current_char}"
            current_char = char
            count = 1
    
    yield f"{count}{current_char}"

def encode_string(text):
    encoded_chars = rle_encode(text)
    return "".join(encoded_chars)

if __name__ == '__main__':
    sample_text = "AAABBBCCCD"
    result = encode_string(sample_text)
    print(result)