def run_length_encode(s: str) -> list[tuple[str, int]]:
    if not s:
        return []

    result = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1

    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_string = "aaabbc"
    encoded = run_length_encode(sample_string)
    print(encoded)

    empty_string = ""
    encoded_empty = run_length_encode(empty_string)
    print(encoded_empty)

    single_char = "x"
    encoded_single = run_length_encode(single_char)
    print(encoded_single)

    alternating = "abab"
    encoded_alternating = run_length_encode(alternating)
    print(encoded_alternating)