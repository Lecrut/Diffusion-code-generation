def run_length_encode(text):
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
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    
    result.append(str(count) + current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbc"
    encoded_text = run_length_encode(sample_text)
    print(encoded_text)
    
    empty_text = ""
    encoded_empty = run_length_encode(empty_text)
    print(repr(encoded_empty))
    
    single_char_text = "a"
    encoded_single = run_length_encode(single_char_text)
    print(encoded_single)
    
    repeated_text = "wwwwww"
    encoded_repeated = run_length_encode(repeated_text)
    print(encoded_repeated)