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
    sample_texts = [
        "AABBBCCCC",
        "ABC",
        "AAAAAAAAAA",
        "",
        "X",
        "AAABBBCCCDDDDEEEEE"
    ]
    
    for sample in sample_texts:
        encoded = run_length_encode(sample)
        print(f"{sample!r} -> {encoded!r}")