def run_length_encode(s):
    if not s:
        return ''
    encoded = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(current_char)
            encoded.append(str(count))
            current_char = s[i]
            count = 1
    encoded.append(current_char)
    encoded.append(str(count))
    return ''.join(encoded)

if __name__ == '__main__':
    sample_input = "aaabbc"
    result = run_length_encode(sample_input)
    print(result)
    sample_input_2 = "aabbcc"
    result_2 = run_length_encode(sample_input_2)
    print(result_2)
    sample_input_3 = ""
    result_3 = run_length_encode(sample_input_3)
    print(result_3)
    sample_input_4 = "zzzzzz"
    result_4 = run_length_encode(sample_input_4)
    print(result_4)