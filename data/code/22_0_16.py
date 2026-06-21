def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    compressed = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = char
            count = 1
            
    compressed.append(f"{count}{current_char}")
    
    return "".join(compressed)

if __name__ == '__main__':
    original = "AAAABBBCCDAA"
    result = run_length_encode(original)
    print(result)