def run_length_encode(sequence):
    if not sequence:
        return ""
    
    encoded_chars = []
    count = 1
    prev_char = sequence[0]
    
    for current_char in sequence[1:]:
        if current_char == prev_char:
            count += 1
        else:
            encoded_chars.append(f"{count}{prev_char}")
            prev_char = current_char
            count = 1
    encoded_chars.append(f"{count}{prev_char}")
    return "".join(encoded_chars)

def run_length_decode(encoded_string):
    if not encoded_string:
        return ""
    
    decoded_chars = []
    i = 0
    length = len(encoded_string)
    
    while i < length:
        count_str = ""
        while i < length and encoded_string[i].isdigit():
            count_str += encoded_string[i]
            i += 1
        if i < length:
            count = int(count_str)
            char = encoded_string[i]
            decoded_chars.append(char * count)
            i += 1
            
    return "".join(decoded_chars)

if __name__ == '__main__':
    original = "aabcccccaaa"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)