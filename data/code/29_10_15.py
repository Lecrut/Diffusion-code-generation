def encode_repeated_chars(text: str) -> str:
    if not text:
        return ""
    
    result = []
    count = 1
    current_char = text[0]
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1
    
    result.append(current_char + str(count))
    return "".join(result)

if __name__ == '__main__':
    print(encode_repeated_chars("aaabbbccca"))