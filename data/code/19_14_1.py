def run_length_encode(s):
    if not s:
        return ''
    
    compressed = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    
    compressed.append(f"{count}{current_char}")
    return ''.join(compressed)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    result = run_length_encode(sample_string)
    print(result)