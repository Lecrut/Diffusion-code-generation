def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
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
    if not encoded:
        return ""
    
    result = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        i += 1
        count_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        count = int(count_str) if count_str else 1
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    sample_inputs = [
        "AAABBBCCDAA",
        "ABC",
        "A",
        "",
        "AAAABBBCCDAA",
        "abbbccca"
    ]
    
    for s in sample_inputs:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(f"Original: '{s}' -> Encoded: '{encoded}' -> Decoded: '{decoded}'")