def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            if count > 3:
                result.append(f"{count}{current_char}")
            else:
                for _ in range(count):
                    result.append(current_char)
            current_char = char
            count = 1
            
    if count > 3:
        result.append(f"{count}{current_char}")
    else:
        for _ in range(count):
            result.append(current_char)
            
    return "".join(result)

if __name__ == '__main__':
    print(run_length_encode("aaabbbcccc"))
    print(run_length_encode("abc"))
    print(run_length_encode(""))
    print(run_length_encode("aaabbbccc"))