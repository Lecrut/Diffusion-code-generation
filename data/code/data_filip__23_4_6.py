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
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

def run_length_decode(s):
    if not s:
        return ""
    
    decoded = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num_str = ""
            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1
            count = int(num_str)
            if i < len(s):
                decoded.append(s[i] * count)
                i += 1
        else:
            decoded.append(s[i])
            i += 1
    
    return "".join(decoded)

if __name__ == '__main__':
    test_string = "AAABBBCCCCD"
    encoded = run_length_encode(test_string)
    print(encoded)
    
    test_string2 = "A1B2C3"
    decoded = run_length_decode("3A2B4C1D")
    print(decoded)
    
    test_string3 = "XYZXYZXYZ"
    encoded3 = run_length_encode(test_string3)
    print(encoded3)
    
    test_string4 = "111122233"
    encoded4 = run_length_encode(test_string4)
    print(encoded4)
    
    decoded4 = run_length_decode(encoded4)
    print(decoded4)