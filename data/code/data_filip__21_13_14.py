def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    count = 1
    prev_char = text[0]
    
    for i in range(1, len(text)):
        current_char = text[i]
        if current_char == prev_char:
            count += 1
        else:
            result.append(f"{prev_char}{count}")
            prev_char = current_char
            count = 1
            
    result.append(f"{prev_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    text = "aabcccccaaa"
    encoded = run_length_encode(text)
    print(encoded)