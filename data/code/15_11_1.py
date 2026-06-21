def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
            
    encoded.append(str(count) + current_char)
    
    return "".join(encoded)

if __name__ == "__main__":
    sample_strings = [
        "aabbbcccc",
        "abc",
        "aaaaa",
        "",
        "a",
        "aabbcc",
        "xyyzww"
    ]
    
    for sample in sample_strings:
        result = run_length_encode(sample)
        print(result)