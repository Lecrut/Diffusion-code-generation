def run_length_encode(text):
    if not text:
        return ""
    
    encoded = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def run_length_decode(encoded):
    if not encoded:
        return ""
    
    decoded = []
    i = 0
    while i < len(encoded):
        count_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        
        if not count_str or i >= len(encoded):
            break
            
        count = int(count_str)
        char = encoded[i]
        i += 1
        
        decoded.append(char * count)
    
    return "".join(decoded)

if __name__ == '__main__':
    sample_input = "AAABBBCCD"
    encoded = run_length_encode(sample_input)
    print(encoded)
    
    decoded = run_length_decode(encoded)
    print(decoded)
    
    sample_input2 = "XYZ"
    encoded2 = run_length_encode(sample_input2)
    print(encoded2)
    
    decoded2 = run_length_decode(encoded2)
    print(decoded2)
    
    sample_input3 = ""
    encoded3 = run_length_encode(sample_input3)
    print(encoded3)
    
    decoded3 = run_length_decode(encoded3)
    print(decoded3)