def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(current_char)
            encoded.append(str(count))
            current_char = s[i]
            count = 1
    
    encoded.append(current_char)
    encoded.append(str(count))
    
    return "".join(encoded)

def run_length_decode(encoded):
    if not encoded:
        return ""
    
    decoded = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        i += 1
        
        num_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        
        if num_str:
            count = int(num_str)
        else:
            count = 1
        
        decoded.append(char * count)
    
    return "".join(decoded)

if __name__ == '__main__':
    sample1 = "aabcccccaaa"
    sample2 = "abc"
    sample3 = ""
    sample4 = "a"
    sample5 = "pppppppp"
    
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))
    
    encoded1 = "a2b1c5a3"
    encoded2 = "a1b1c1"
    encoded3 = ""
    
    print(run_length_decode(encoded1))
    print(run_length_decode(encoded2))
    print(run_length_decode(encoded3))