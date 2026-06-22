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
            encoded.append(current_char)
            encoded.append(str(count))
            current_char = char
            count = 1

    encoded.append(current_char)
    encoded.append(str(count))

    return "".join(encoded)

if __name__ == "__main__":
    sample_input = "AAABBBCCDAA"
    result = run_length_encode(sample_input)
    print(result)

    empty_input = ""
    result_empty = run_length_encode(empty_input)
    print(result_empty)

    single_char = "Z"
    result_single = run_length_encode(single_char)
    print(result_single)

    mixed_input = "abcdef"
    result_mixed = run_length_encode(mixed_input)
    print(result_mixed)

    long_run = "AAAAAA"
    result_long = run_length_encode(long_run)
    print(result_long)