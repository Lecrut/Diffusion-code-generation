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
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

def run_length_decode(encoded_s):
    if not encoded_s:
        return ""
    
    result = []
    i = 0
    n = len(encoded_s)
    
    while i < n:
        if encoded_s[i].isdigit():
            num_str = ""
            while i < n and encoded_s[i].isdigit():
                num_str += encoded_s[i]
                i += 1
            count = int(num_str)
            if i < n:
                char = encoded_s[i]
                i += 1
                result.append(char * count)
        else:
            result.append(encoded_s[i])
            i += 1
    
    return "".join(result)

if __name__ == '__main__':
    sample_inputs = [
        "aabcccccaaa",
        "abcd",
        "a",
        "",
        "aaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbb",
        "abcabcabc",
        "xxyyzz"
    ]
    
    for s in sample_inputs:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(encoded)
        print(decoded)