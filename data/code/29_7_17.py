def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == '__main__':
    samples = [
        "",
        "A",
        "AAA",
        "AABCCDDDD",
        "abcde",
        "AAAAABBBBBCCCCCC",
        "hello world",
        "1223334444",
        "!@#$%^&*()",
        "AaBbCcDdEeFf"
    ]
    
    for sample in samples:
        result = run_length_encode(sample)
        print(f"Input: {sample!r}\nOutput: {result!r}\n")