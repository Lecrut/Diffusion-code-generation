def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    count = 1
    length = len(text)
    
    for i in range(1, length):
        current_char = text[i]
        previous_char = text[i - 1]
        
        if current_char == previous_char:
            count += 1
        else:
            result.append(f"{count}{previous_char}")
            count = 1
    
    result.append(f"{count}{text[-1]}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbc"
    encoded = run_length_encode(sample_text)
    print(encoded)
    
    sample_unicode = "你好你好世界"
    unicode_encoded = run_length_encode(sample_unicode)
    print(unicode_encoded)