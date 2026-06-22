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
    print(run_length_encode("AABCCDD"))
    print(run_length_encode(""))
    print(run_length_encode("A"))
    print(run_length_encode("AAAAA"))
    print(run_length_encode("ABC"))