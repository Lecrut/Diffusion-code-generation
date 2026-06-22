def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    if len(text) == 1:
        return "1" + text
    
    result = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = text[i]
            count = 1
    
    result.append(str(count) + current_char)
    
    return "".join(result)

if __name__ == '__main__':
    print(run_length_encode("aabcccccaaa"))
    print(run_length_encode(""))
    print(run_length_encode("z"))