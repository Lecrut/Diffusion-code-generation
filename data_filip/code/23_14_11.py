def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    count = 1
    current_char = s[0]
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == "__main__":
    print(run_length_encode("aaaabbbcc"))
    print(run_length_encode("aabccddd"))
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("abcdef"))