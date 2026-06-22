def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    length = len(input_string)
    
    i = 1
    while i < length:
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            if count >= 3:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char * count)
            current_char = char
            count = 1
        i += 1
    
    if count >= 3:
        result.append(f"{count}{current_char}")
    else:
        result.append(current_char * count)
        
    return "".join(result)

if __name__ == '__main__':
    print(run_length_encode("aaabbbcc"))
    print(run_length_encode("aab"))
    print(run_length_encode("abc"))
    print(run_length_encode("aaaabbbcc"))