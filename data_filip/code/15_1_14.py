def compress_string(input_string):
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_data = 'aaaaabbbbcccd'
    compressed_result = compress_string(sample_data)
    print(compressed_result)