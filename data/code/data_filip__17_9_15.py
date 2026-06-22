def run_length_encode(text):
    if not text:
        return ""
    
    result = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    result.append(f"{current_char}{count}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_text = "AAABBBCCD"
    encoded_result = run_length_encode(sample_text)
    print(encoded_result)
    
    empty_text = ""
    empty_result = run_length_encode(empty_text)
    print(empty_result)
    
    single_char_text = "A"
    single_char_result = run_length_encode(single_char_text)
    print(single_char_result)