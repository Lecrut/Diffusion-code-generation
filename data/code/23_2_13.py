def run_length_encode(s):
    if not s:
        return ""
    
    encoded_chars = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded_chars.append(str(count))
            encoded_chars.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        encoded_chars.append(str(count))
    encoded_chars.append(current_char)
    
    return "".join(encoded_chars)

def run_length_decode(s):
    if not s:
        return ""
    
    decoded_chars = []
    count = []
    
    for char in s:
        if char.isdigit():
            count.append(char)
        else:
            if count:
                repeat_count = int("".join(count))
                count = []
            else:
                repeat_count = 1
            decoded_chars.append(char * repeat_count)
            
    return "".join(decoded_chars)

if __name__ == '__main__':
    original_string = "aaabbbbcc"
    encoded = run_length_encode(original_string)
    print(encoded)
    
    decoded = run_length_decode(encoded)
    print(decoded)