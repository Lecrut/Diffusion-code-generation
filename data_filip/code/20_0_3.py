def run_length_encode(text):
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

def run_length_decode(encoded):
    decoded = []
    for char, count in encoded:
        decoded.append(char * count)
    return "".join(decoded)

if __name__ == '__main__':
    original = "AAABBBCC"
    encoded_data = run_length_encode(original)
    print(encoded_data)
    decoded_text = run_length_decode(encoded_data)
    print(decoded_text)