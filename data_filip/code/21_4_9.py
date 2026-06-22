def run_length_encode(text: str) -> dict:
    if not text:
        return {}
    
    encoded_list = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            encoded_list.append((current_char, count))
            current_char = char
            count = 1
    encoded_list.append((current_char, count))
    
    return {f"{char}{count}": count for char, count in encoded_list}

if __name__ == '__main__':
    sample_text = "aaabbc"
    result = run_length_encode(sample_text)
    print(result)