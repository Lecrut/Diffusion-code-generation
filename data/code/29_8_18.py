def encode_repeating_chars(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{current_char}{count}")
            else:
                result.append(current_char)
            current_char = s[i]
            count = 1
    if count > 1:
        result.append(f"{current_char}{count}")
    else:
        result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbcdddd"
    encoded_result = encode_repeating_chars(sample_input)
    print(encoded_result)
    sample_input_2 = "aabbba"
    encoded_result_2 = encode_repeating_chars(sample_input_2)
    print(encoded_result_2)