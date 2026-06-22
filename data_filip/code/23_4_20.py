def run_length_encode(text):
    if not text:
        return ""
    
    encoded = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(current_char)
            current_char = text[i]
            count = 1
    
    encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

def run_length_decode(encoded_text):
    if not encoded_text:
        return ""
    
    decoded = []
    i = 0
    n = len(encoded_text)
    
    while i < n:
        count_str = ""
        while i < n and encoded_text[i].isdigit():
            count_str += encoded_text[i]
            i += 1
        
        if i < n:
            char = encoded_text[i]
            i += 1
            repeat_count = int(count_str)
            decoded.append(char * repeat_count)
    
    return "".join(decoded)

if __name__ == '__main__':
    sample_text = "aaabbbcccdd"
    encoded = run_length_encode(sample_text)
    print(encoded)
    
    decoded = run_length_decode(encoded)
    print(decoded)
    
    sample_text_multi = "a12b3c"
    encoded_multi = run_length_encode(sample_text_multi)
    print(encoded_multi)
    
    decoded_multi = run_length_decode("3a2b4c")
    print(decoded_multi)