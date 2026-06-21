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
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    sample = "AAABBBCCDAA"
    print(run_length_encode(sample))
    sample2 = "ABC"
    print(run_length_encode(sample2))
    sample3 = "A"
    print(run_length_encode(sample3))
    sample4 = ""
    print(run_length_encode(sample4))
    sample5 = "1122333!!@"
    print(run_length_encode(sample5))