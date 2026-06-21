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
    decoded_chars = []
    for char, count in encoded:
        decoded_chars.append(char * count)
    return ''.join(decoded_chars)

if __name__ == '__main__':
    sample1 = "AAABBBCCD"
    sample2 = "XYZ"
    sample3 = ""
    
    encoded1 = run_length_encode(sample1)
    decoded1 = run_length_decode(encoded1)
    
    encoded2 = run_length_encode(sample2)
    decoded2 = run_length_decode(encoded2)
    
    encoded3 = run_length_encode(sample3)
    decoded3 = run_length_decode(encoded3)
    
    print(encoded1)
    print(decoded1)
    print(encoded2)
    print(decoded2)
    print(encoded3)
    print(decoded3)