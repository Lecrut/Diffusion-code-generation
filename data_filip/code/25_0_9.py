def run_length_encode(s):
    if not s:
        return []

    result = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = s[i]
            count = 1

    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_string = "AAABBBCCCDAA"
    encoded = run_length_encode(sample_string)
    print(encoded)

    empty_string = ""
    encoded_empty = run_length_encode(empty_string)
    print(encoded_empty)

    single_char = "X"
    encoded_single = run_length_encode(single_char)
    print(encoded_single)

    mixed_string = "ABABAB"
    encoded_mixed = run_length_encode(mixed_string)
    print(encoded_mixed)

    long_run = "AAAAA"
    encoded_long = run_length_encode(long_run)
    print(encoded_long)