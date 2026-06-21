def compress_text(text: str) -> str:
    if not text:
        return ""
    
    result = []
    count = 1
    n = len(text)
    
    i = 1
    while i < n:
        if text[i] == text[i - 1]:
            count += 1
        else:
            if count > 3:
                result.append(f"{count}{text[i - 1]}")
            elif count > 1:
                result.append(text[i - 1] * count)
            else:
                result.append(text[i - 1])
            count = 1
        i += 1
    
    if count > 3:
        result.append(f"{count}{text[-1]}")
    elif count > 1:
        result.append(text[-1] * count)
    else:
        result.append(text[-1])
    
    compressed = "".join(result)
    
    if len(compressed) >= len(text):
        return text
    
    return compressed

if __name__ == '__main__':
    sample = "aaabbbcccddeff"
    output = compress_text(sample)
    print(output)