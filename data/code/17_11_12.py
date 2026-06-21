def run_length_encode(s: str) -> str:
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

if __name__ == '__main__':
    sample = "aabcccccaaa"
    result = run_length_encode(sample)
    print(result)

    sample2 = "ABC"
    result2 = run_length_encode(sample2)
    print(result2)

    sample3 = ""
    result3 = run_length_encode(sample3)
    print(repr(result3))

    sample4 = "a"
    result4 = run_length_encode(sample4)
    print(result4)