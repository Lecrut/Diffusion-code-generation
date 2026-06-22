def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    encoded = []
    count = 1
    prev_char = text[0]
    
    for i in range(1, len(text)):
        current_char = text[i]
        if current_char == prev_char:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(prev_char)
            prev_char = current_char
            count = 1
    
    encoded.append(str(count))
    encoded.append(prev_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    result = run_length_encode("AAABBBCCDAA")
    print(result)