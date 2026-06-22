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
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    return "".join(encoded)

if __name__ == '__main__':
    print(run_length_encode("aabbbc"))
    print(run_length_encode("abcd"))
    print(run_length_encode("aaabbaac"))
    print(run_length_encode(""))
    print(run_length_encode("a"))