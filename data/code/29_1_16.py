def compress_string(input_str: str) -> str:
    if not input_str:
        return ""
    
    result = []
    current_char = input_str[0]
    count = 1
    
    for i in range(1, len(input_str)):
        if input_str[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = input_str[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    output = compress_string(sample_input)
    print(output)