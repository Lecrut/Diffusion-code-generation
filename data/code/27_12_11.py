def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    encoded_parts = []
    count = 1
    length = len(text)
    
    for i in range(1, length):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded_parts.append(f"{count}{text[i - 1]}")
            count = 1
    encoded_parts.append(f"{count}{text[length - 1]}")
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_text = "aabcccccaaa"
    result = run_length_encode(sample_text)
    print(result)