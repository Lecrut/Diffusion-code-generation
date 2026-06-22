def compress_rle(input_string):
    if not input_string:
        return ""
    
    result = []
    count = 1
    current_char = input_string[0]
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbc"
    output = compress_rle(sample_input)
    print(output)