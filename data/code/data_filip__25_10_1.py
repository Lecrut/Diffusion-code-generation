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
            result.append(f"{count}{current_char}")
            current_char = input_str[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    
    compressed = "".join(result)
    
    if len(compressed) >= len(input_str):
        return input_str
    
    return compressed

if __name__ == '__main__':
    sample = "aabcccccaaa"
    print(compress_string(sample))
    
    empty = ""
    print(compress_string(empty))
    
    single = "a"
    print(compress_string(single))