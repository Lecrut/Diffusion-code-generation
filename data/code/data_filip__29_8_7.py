def encode_repeating_chars(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = s[i]
            count = 1
    result.append(current_char)
    result.append(str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbcccc"
    encoded_result = encode_repeating_chars(sample_input)
    print(encoded_result)