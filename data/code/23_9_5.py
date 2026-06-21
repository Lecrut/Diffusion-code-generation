def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    count = 1
    length = len(s)
    current_char = s[0]
    
    index = 1
    while index < length:
        char = s[index]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
        index += 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbc"
    encoded = run_length_encode(sample_string)
    print(encoded)