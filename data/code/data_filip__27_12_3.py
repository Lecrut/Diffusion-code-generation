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

if __name__ == "__main__":
    sample_strings = [
        "AAAABBBCCDAA",
        "ABC",
        "AAAAAAAAAA",
        "AABBCCDD",
        "",
        "A"
    ]
    
    for s in sample_strings:
        encoded = run_length_encode(s)
        print(f"Input: '{s}' -> Output: '{encoded}'")