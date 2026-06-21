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
    return ''.join(result)

if __name__ == '__main__':
    sample_texts = ["AABCCCDEEEE", "ABC", "AAAAA", "ABABAB", ""]
    for text in sample_texts:
        encoded = run_length_encode(text)
        print(f"{text} -> {encoded}")