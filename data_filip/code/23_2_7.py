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

def run_length_decode(s):
    if not s:
        return ""
    
    result = []
    count_str = []
    
    for char in s:
        if char.isdigit():
            count_str.append(char)
        else:
            count = int("".join(count_str))
            result.append(char * count)
            count_str = []
    
    return "".join(result)

if __name__ == '__main__':
    original = "aaabbbbcccd"
    encoded = run_length_encode(original)
    print(encoded)
    
    decoded = run_length_decode(encoded)
    print(decoded)