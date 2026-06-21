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
            encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1

    encoded.append(str(count))
    encoded.append(current_char)

    return "".join(encoded)

if __name__ == '__main__':
    sample1 = "aabcccccaaa"
    sample2 = "abc"
    sample3 = ""
    sample4 = "bbbbbbbbbbbbbbbbbbbbbbbbbb"
    sample5 = "a"

    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))