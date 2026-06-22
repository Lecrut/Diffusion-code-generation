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

if __name__ == "__main__":
    sample_string = "AAABBBCCDAA"
    encoded = run_length_encode(sample_string)
    print(encoded)
    
    sample_string2 = "ABC"
    encoded2 = run_length_encode(sample_string2)
    print(encoded2)
    
    sample_string3 = ""
    encoded3 = run_length_encode(sample_string3)
    print(encoded3)
    
    sample_string4 = "A"
    encoded4 = run_length_encode(sample_string4)
    print(encoded4)
    
    sample_string5 = "AAAABBBCCDAA"
    encoded5 = run_length_encode(sample_string5)
    print(encoded5)