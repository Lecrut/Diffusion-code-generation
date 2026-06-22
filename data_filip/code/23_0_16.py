def run_length_encode(text):
    if not text:
        return text
    
    result = []
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]
        count = 1
        while i + count < n and text[i + count] == char:
            count += 1
        
        if count > 1:
            result.append(str(count))
        result.append(char)
        i += count
    
    encoded = ''.join(result)
    
    if len(encoded) >= n:
        return text
    
    return encoded

if __name__ == '__main__':
    samples = [
        "",
        "A",
        "AB",
        "AA",
        "AABBCC",
        "AAAAAA",
        "AABBBCCCC",
        "ABC",
        "XYZXYZ",
        "aabbcc",
        "112233",
        "Mississippi",
        "AABCCCCCDDDEEE",
        "HelloWorld",
        "NoDuplicatesHere"
    ]
    
    for sample in samples:
        encoded = run_length_encode(sample)
        print(encoded)