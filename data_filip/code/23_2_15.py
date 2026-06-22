def run_length_encode(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

def run_length_decode(s):
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        if not num_str:
            result.append(char)
        else:
            result.append(char * int(num_str))
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbbcccaaa"
    encoded = run_length_encode(sample_input)
    decoded = run_length_decode(encoded)
    print(f"Original: {sample_input}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")