def run_length_encoding(s):
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
    sample_string = "aaabbcccc"
    print(run_length_encoding(sample_string))
    empty_string = ""
    print(run_length_encoding(empty_string))
    single_char = "z"
    print(run_length_encoding(single_char))
    mixed_string = "aAa11"
    print(run_length_encoding(mixed_string))