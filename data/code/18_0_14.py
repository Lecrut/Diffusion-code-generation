def run_length_encode(s):
    if not s:
        return []
    
    encoded_list = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            encoded_list.append((current_char, count))
            current_char = char
            count = 1
    
    encoded_list.append((current_char, count))
    
    return encoded_list

if __name__ == '__main__':
    text = "aaabbccc"
    result = run_length_encode(text)
    print(result)