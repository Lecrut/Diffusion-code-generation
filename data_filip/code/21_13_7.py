def run_length_encode(text):
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = text[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aabcccccaaa"
    encoded = run_length_encode(sample_text)
    print(encoded)
    
    single_char = "z"
    encoded_single = run_length_encode(single_char)
    print(encoded_single)
    
    empty_string = ""
    encoded_empty = run_length_encode(empty_string)
    print(encoded_empty)
    
    mixed = "ABCDD"
    encoded_mixed = run_length_encode(mixed)
    print(encoded_mixed)