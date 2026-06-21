def run_length_encode(s):
    if not s:
        return ""
    
    result_parts = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result_parts.append(str(count) + current_char)
            current_char = s[i]
            count = 1
            
    result_parts.append(str(count) + current_char)
    
    return "".join(result_parts)

if __name__ == '__main__':
    sample_inputs = [
        "AAAABBBCCDAA",
        "A",
        "",
        "ABC",
        "AAAAAAAAAA",
        "AABBBBCCCDDDDDDDEEEEEEFFG"
    ]
    
    for s in sample_inputs:
        encoded = run_length_encode(s)
        print(f"Input: '{s}' -> Encoded: '{encoded}'")