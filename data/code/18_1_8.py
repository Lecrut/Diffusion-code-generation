def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded_chars = []
    i = 0
    length = len(input_string)
    
    while i < length:
        current_char = input_string[i]
        count = 1
        
        while i + count < length and input_string[i + count] == current_char:
            count += 1
        
        encoded_chars.append(str(count))
        encoded_chars.append(current_char)
        
        i += count
    
    return "".join(encoded_chars)

if __name__ == '__main__':
    sample_text = "AAAABBBCCDAA"
    result = run_length_encode(sample_text)
    print(result)