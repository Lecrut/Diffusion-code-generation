def encode_string(s):
    if not s:
        return ""
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        current_char = s[i]
        count = 1
        j = i + 1
        while j < n and s[j] == current_char:
            count += 1
            j += 1
        result.append(f"{current_char}{count}")
        i = j
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    encoded_output = encode_string(sample_input)
    print(encoded_output)