def rle_encode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_inputs = [
        "",
        "a",
        "aaa",
        "aabbc",
        "aabbccddeeff",
        "hello world",
        "zzzzzaaabbcccc"
    ]
    
    for sample in sample_inputs:
        encoded = rle_encode(sample)
        print(encoded)