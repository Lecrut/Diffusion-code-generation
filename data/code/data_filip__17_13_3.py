import io

def encode_run_length(input_string):
    if not input_string:
        return ""
    
    result = io.StringIO()
    current_char = input_string[0]
    count = 1
    length = len(input_string)
    
    for i in range(1, length):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.write(f"{current_char}{count}")
            current_char = char
            count = 1
    result.write(f"{current_char}{count}")
    
    return result.getvalue()

def decode_run_length(input_string):
    if not input_string:
        return ""
    
    result = io.StringIO()
    length = len(input_string)
    i = 0
    
    while i < length:
        char = input_string[i]
        i += 1
        if i >= length:
            result.write(char)
            break
            
        count_str = ""
        next_char = input_string[i]
        
        while not next_char.isalpha() and i < length:
            count_str += next_char
            i += 1
            if i < length:
                next_char = input_string[i]
        
        count = int(count_str) if count_str else 1
        result.write(char * count)
        
    return result.getvalue()

if __name__ == '__main__':
    original = "aabcccccaaa"
    encoded = encode_run_length(original)
    decoded = decode_run_length(encoded)
    print(encode_run_length("aabcccccaaa"))
    print(decode_run_length("a2b1c5a3"))