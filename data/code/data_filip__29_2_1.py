def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    length = len(s)
    
    for i in range(1, length):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
    
    encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    input_string = "aaabbc"
    result = run_length_encode(input_string)
    print(result)