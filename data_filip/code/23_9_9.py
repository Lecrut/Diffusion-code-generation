def run_length_encode(s):
    if not s:
        return ""
    result = []
    n = len(s)
    i = 0
    while i < n:
        count = 1
        current_char = s[i]
        i += 1
        while i < n and s[i] == current_char:
            count += 1
            i += 1
        result.append(str(count) + current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccccdddddeeeeffff"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)
    sample_input_2 = "Hello World"
    encoded_output_2 = run_length_encode(sample_input_2)
    print(encoded_output_2)
    sample_input_3 = ""
    encoded_output_3 = run_length_encode(sample_input_3)
    print(encoded_output_3)
    sample_input_4 = "A"
    encoded_output_4 = run_length_encode(sample_input_4)
    print(encoded_output_4)
    sample_input_5 = "AABBCC"
    encoded_output_5 = run_length_encode(sample_input_5)
    print(encoded_output_5)