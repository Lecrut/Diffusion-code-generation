def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    return "".join(result)

def run_length_decode(encoded: str) -> str:
    decoded = []
    i = 0
    
    while i < len(encoded):
        char = encoded[i]
        j = i + 1
        while j < len(encoded) and encoded[j].isdigit():
            j += 1
        count = int(encoded[i+1:j])
        decoded.append(char * count)
        i = j
    
    return "".join(decoded)

if __name__ == '__main__':
    samples = [
        "AAABBBCCD",
        "ABCDE",
        "AABBCCCDDDD",
        "",
        "A",
        "AAAAA",
        "Hello World!"
    ]
    
    for sample in samples:
        encoded = run_length_encode(sample)
        decoded = run_length_decode(encoded)
        print(f"Original: {sample!r}")
        print(f"Encoded:  {encoded!r}")
        print(f"Decoded:  {decoded!r}")
        print()