def encode_run_length(s):
    result = {}
    if not s:
        return result
    current_char = s[0]
    current_count = 1
    for char in s[1:]:
        if not char.isalnum():
            continue
        if char == current_char:
            current_count += 1
        else:
            result[current_char] = current_count
            current_char = char
            current_count = 1
    result[current_char] = current_count
    return result

if __name__ == '__main__':
    sample_string = "aaabbbccdd"
    encoded = encode_run_length(sample_string)
    print(encoded)