def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    
    encoded.append(str(count) + current_char)
    
    return "".join(encoded)

def run_length_decode(s):
    if not s:
        return ""
    
    decoded = []
    i = 0
    
    while i < len(s):
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        
        if num_str:
            count = int(num_str)
        else:
            count = 1
        
        if i < len(s):
            char = s[i]
            decoded.append(char * count)
            i += 1
        else:
            break
    
    return "".join(decoded)

if __name__ == '__main__':
    sample_input = "AABBBCCCCDDDDDEEEEEEEFFFFGG"
    encoded = run_length_encode(sample_input)
    decoded = run_length_decode(encoded)
    
    print("Original:", sample_input)
    print("Encoded:", encoded)
    print("Decoded:", decoded)
    
    sample2 = "AAABBC"
    encoded2 = run_length_encode(sample2)
    print("Encoded sample2:", encoded2)
    
    sample3 = "111223333"
    encoded3 = run_length_encode(sample3)
    print("Encoded sample3:", encoded3)
    
    empty = ""
    encoded_empty = run_length_encode(empty)
    print("Encoded empty:", encoded_empty)
    
    single = "A"
    encoded_single = run_length_encode(single)
    print("Encoded single:", encoded_single)