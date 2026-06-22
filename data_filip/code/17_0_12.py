def run_length_encode(input_string):
    if not input_string:
        return ""
    encoded_parts = []
    current_char = input_string[0]
    count = 1
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(current_char + str(count))
            current_char = char
            count = 1
    encoded_parts.append(current_char + str(count))
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_inputs = [
        "aaabbc",
        "aabcccccaaa",
        "abcdef",
        "AAAA",
        "AABBBCCCCDD",
        "single",
        "",
        "11122233"
    ]
    for sample in sample_inputs:
        result = run_length_encode(sample)
        print(result)