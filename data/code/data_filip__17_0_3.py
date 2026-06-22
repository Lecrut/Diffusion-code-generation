def run_length_encode(input_string):
    if not input_string:
        return ""
    
    if len(input_string) == 1:
        return input_string + "1"
    
    encoded_chars = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_chars.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    encoded_chars.append(f"{current_char}{count}")
    
    return "".join(encoded_chars)

if __name__ == '__main__':
    sample_text = "AAAABBBCCDAA"
    result = run_length_encode(sample_text)
    print(result)