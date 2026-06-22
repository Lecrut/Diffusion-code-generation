def run_length_encode(input_str):
    if not input_str:
        return ""
    
    result = []
    count = 1
    current_char = input_str[0]
    
    for char in input_str[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    text = "AABCCCDEEEE"
    encoded = run_length_encode(text)
    print(encoded)