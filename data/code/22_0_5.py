def run_length_encode(s: str) -> str:
    if not s:
        return ""

    result = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1

    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample_input = "AAABBBCCDAA"
    compressed = run_length_encode(sample_input)
    print(compressed)

    sample_input2 = "abcdef"
    compressed2 = run_length_encode(sample_input2)
    print(compressed2)

    sample_input3 = ""
    compressed3 = run_length_encode(sample_input3)
    print(compressed3)

    sample_input4 = "A"
    compressed4 = run_length_encode(sample_input4)
    print(compressed4)

    sample_input5 = "AA"
    compressed5 = run_length_encode(sample_input5)
    print(compressed5)