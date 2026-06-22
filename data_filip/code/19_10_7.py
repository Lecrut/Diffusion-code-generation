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
            result.append(f"{count}{current_char}")
            current_char = text[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_strings = [
        "aaaabbbcc",
        "abcdef",
        "aabbcc",
        "",
        "zzzzzzzzz",
        "a1b2c3",
        "hello world"
    ]
    
    for s in sample_strings:
        encoded = run_length_encode(s)
        print(f"Input: '{s}'\nOutput: '{encoded}'\n")