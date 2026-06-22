def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == "__main__":
    print(run_length_encode("aaabbc"))
    print(run_length_encode("aabcccccaaa"))
    print(run_length_encode("xyz"))
    print(run_length_encode(""))
    print(run_length_encode("a"))