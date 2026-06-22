def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

def run_length_decode(encoded):
    if not encoded:
        return ""
    
    result = []
    i = 0
    while i < len(encoded):
        count = 0
        while i < len(encoded) and encoded[i].isdigit():
            count = count * 10 + int(encoded[i])
            i += 1
        
        if i < len(encoded):
            char = encoded[i]
            i += 1
            if count == 0:
                count = 1
            result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCCDDE"
    encoded = run_length_encode(sample_input)
    print(encoded)
    
    decoded = run_length_decode(encoded)
    print(decoded)
    
    empty_input = ""
    encoded_empty = run_length_encode(empty_input)
    print(encoded_empty)
    
    single_char = "Z"
    encoded_single = run_length_encode(single_char)
    print(encoded_single)
    
    long_run = "A" * 15
    encoded_long = run_length_encode(long_run)
    print(encoded_long)