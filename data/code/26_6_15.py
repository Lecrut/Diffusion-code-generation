def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def run_length_decode(s):
    if not s:
        return ""
    
    decoded = []
    i = 0
    
    while i < len(s):
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        
        if count_str:
            count = int(count_str)
            if i < len(s):
                char = s[i]
                decoded.append(char * count)
                i += 1
    
    return "".join(decoded)

if __name__ == '__main__':
    sample = "AAABBBCCCDDDEE"
    encoded = run_length_encode(sample)
    decoded = run_length_decode(encoded)
    print(f"Original: {sample}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    
    empty = ""
    print(run_length_encode(empty))
    print(run_length_decode(""))
    
    single = "Z"
    print(run_length_encode(single))
    print(run_length_decode(run_length_encode(single)))