def run_length_encode(s):
    if not s:
        return ""
    
    shifted = ' ' + s[:-1]
    result = []
    current_char = s[0]
    count = 1
    
    for char, prev_char in zip(s, shifted):
        if char == prev_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    input_string = 'AAAAABBBB'
    encoded = run_length_encode(input_string)
    print(encoded)