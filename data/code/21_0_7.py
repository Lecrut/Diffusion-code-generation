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
    sample_string = "aaabbcdd"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)
    sample_string_empty = ""
    encoded_result_empty = run_length_encode(sample_string_empty)
    print(encoded_result_empty)
    sample_string_single = "a"
    encoded_result_single = run_length_encode(sample_string_single)
    print(encoded_result_single)
    sample_string_mixed = "aabcccaad"
    encoded_result_mixed = run_length_encode(sample_string_mixed)
    print(encoded_result_mixed)