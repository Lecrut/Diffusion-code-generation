def run_length_encode(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def run_length_decode(encoded):
    if not encoded:
        return ""
    result = []
    i = 0
    while i < len(encoded):
        count_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        count = int(count_str) if count_str else 1
        if i < len(encoded):
            char = encoded[i]
            i += 1
            result.append(char * count)
        else:
            break
    return "".join(result)

if __name__ == "__main__":
    sample1 = "AAABBBCCD"
    encoded1 = run_length_encode(sample1)
    decoded1 = run_length_decode(encoded1)
    print(encoded1)
    print(decoded1)
    
    sample2 = "abcdef"
    encoded2 = run_length_encode(sample2)
    decoded2 = run_length_decode(encoded2)
    print(encoded2)
    print(decoded2)
    
    sample3 = "A"
    encoded3 = run_length_encode(sample3)
    decoded3 = run_length_decode(encoded3)
    print(encoded3)
    print(decoded3)
    
    sample4 = ""
    encoded4 = run_length_encode(sample4)
    decoded4 = run_length_decode(encoded4)
    print(encoded4)
    print(decoded4)
    
    sample5 = "AAAAAAAAAAAAAAAA"
    encoded5 = run_length_encode(sample5)
    decoded5 = run_length_decode(encoded5)
    print(encoded5)
    print(decoded5)