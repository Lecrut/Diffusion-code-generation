def run_length_encode(text: str) -> str:
    if not text:
        return text

    result = []
    i = 0
    length = len(text)
    
    while i < length:
        current_char = text[i]
        count = 1
        j = i + 1
        while j < length and text[j] == current_char:
            count += 1
            j += 1
        
        if count > 1:
            result.append(str(count))
        result.append(current_char)
        i = j

    return "".join(result)

if __name__ == '__main__':
    samples = [
        "aabcccccaaa",
        "abc",
        "",
        "aabbcc",
        "a",
    ]

    for sample in samples:
        encoded = run_length_encode(sample)
        print(encoded)