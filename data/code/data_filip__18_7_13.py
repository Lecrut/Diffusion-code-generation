def run_length_encode(input_string):
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    length = len(input_string)
    
    for i in range(1, length):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

def run_length_decode(encoded_string):
    if not encoded_string:
        return ""
    
    result = []
    i = 0
    length = len(encoded_string)
    
    while i < length:
        count_str = ""
        while i < length and encoded_string[i].isdigit():
            count_str += encoded_string[i]
            i += 1
        
        if i < length:
            char = encoded_string[i]
            count = int(count_str)
            result.append(char * count)
            i += 1
    
    return "".join(result)

if __name__ == '__main__':
    original_text = "AAABBBCCD"
    encoded_text = run_length_encode(original_text)
    decoded_text = run_length_decode(encoded_text)
    
    print(encoded_text)
    print(decoded_text)