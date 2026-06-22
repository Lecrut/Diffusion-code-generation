def run_length_encode(s: str) -> list:
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
    sample_string = "AAABBCDDDD"
    encoded = run_length_encode(sample_string)
    print(encoded)

    sample_empty = ""
    encoded_empty = run_length_encode(sample_empty)
    print(encoded_empty)

    sample_single = "Z"
    encoded_single = run_length_encode(sample_single)
    print(encoded_single)

    sample_complex = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_complex = run_length_encode(sample_complex)
    print(encoded_complex)