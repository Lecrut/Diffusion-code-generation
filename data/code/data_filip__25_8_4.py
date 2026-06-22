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
            encoded.append(f"{current_char}{count}")
            current_char = char
            count = 1
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == '__main__':
    sample1 = "AAABBBCCDAA"
    sample2 = "abc"
    sample3 = "111222333"
    sample4 = "hello!!!"
    sample5 = "@@##$$"
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))