def encode_run_length(text):
    if not text:
        return ""
    
    encoded = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = text[i]
            count = 1
    
    encoded.append(f"{count}{current_char}")
    
    return "".join(encoded)

if __name__ == '__main__':
    sample1 = ""
    sample2 = "a"
    sample3 = "aabcccccaaa"
    
    print(encode_run_length(sample1))
    print(encode_run_length(sample2))
    print(encode_run_length(sample3))