def rle_encode(input_string):
    if not input_string:
        return ""
    
    encoded = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    result = rle_encode(sample_input)
    print(result)