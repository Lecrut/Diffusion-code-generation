def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    
    result.append(str(count) + current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAAAABBBCCD"
    encoded_value = run_length_encode(sample_string)
    print(encoded_value)