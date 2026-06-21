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
            encoded.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_strings = ["", "a", "aa", "aaa", "aabbbcccc", "aabbbcccddd", "xyyyzzzz"]
    for sample in sample_strings:
        print(run_length_encode(sample))