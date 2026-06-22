def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    if len(text) == 1:
        return text

    result = []
    current_char = text[0]
    count = 1

    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    
    encoded = "".join(result)
    
    if len(encoded) >= len(text):
        return text
    
    return encoded

if __name__ == '__main__':
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("abc"))
    print(run_length_encode("aabcccccaaa"))
    print(run_length_encode("aaaaaaaaaa"))
    print(run_length_encode("xyz"))