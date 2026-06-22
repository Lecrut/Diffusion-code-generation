def compress_string(input_str):
    if not input_str:
        return ""

    result = []
    current_char = input_str[0]
    count = 1

    for char in input_str[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = char
            count = 1

    result.append(current_char)
    result.append(str(count))

    return "".join(result)

if __name__ == '__main__':
    sample_inputs = [
        "aabcccccaaa",
        "abcd",
        "aaabbbccc",
        "a",
        "",
        "aabbc"
    ]

    for sample in sample_inputs:
        print(compress_string(sample))