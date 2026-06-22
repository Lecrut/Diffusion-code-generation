def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    encoded_parts = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    encoded_parts.append(f"{current_char}{count}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    print(run_length_encode("aabcccccaaa"))
    print(run_length_encode("abc"))
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("aaaaa"))