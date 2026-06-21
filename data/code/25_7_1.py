def is_run_length_effective(original_string):
    if not original_string:
        return len(original_string) <= len("")

    encoded = []
    current_char = original_string[0]
    count = 1

    for char in original_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = char
            count = 1

    encoded.append(f"{current_char}{count}")
    encoded_string = "".join(encoded)

    return len(encoded_string) < len(original_string)

if __name__ == '__main__':
    sample_strings = [
        "AABBBCC",
        "ABC",
        "AAAAAAAAAA",
        "A",
        "",
        "AABBC",
        "XYZXYZ"
    ]

    for s in sample_strings:
        result = is_run_length_effective(s)
        print(result)