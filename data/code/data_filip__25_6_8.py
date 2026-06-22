def run_length_encode(s):
    if not s:
        return ""
    if len(s) == 1:
        return s + "1"
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = char
            count = 1
    
    encoded.append(current_char + str(count))
    return "".join(encoded)

if __name__ == '__main__':
    sample_inputs = ["", "a", "aabbbcccc", "aaaaa", "abcde", "AABBCC"]
    for sample in sample_inputs:
        result = run_length_encode(sample)
        print(result)