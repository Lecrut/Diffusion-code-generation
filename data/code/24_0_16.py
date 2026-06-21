def compress_run_length(input_string):
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    
    result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccaaaddddd"
    compressed = compress_run_length(sample_input)
    print(compressed)
    
    sample_input2 = ""
    compressed2 = compress_run_length(sample_input2)
    print(compressed2)
    
    sample_input3 = "abcdef"
    compressed3 = compress_run_length(sample_input3)
    print(compressed3)