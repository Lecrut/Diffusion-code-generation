def run_length_encoding(s):
    if not s:
        return ""
    result = []
    count = 1
    n = len(s)
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(s[i - 1])
            count = 1
    result.append(str(count))
    result.append(s[n - 1])
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDDDDDEEEE"
    encoded_result = run_length_encoding(sample_input)
    print(encoded_result)
    sample_input_two = "A"
    encoded_result_two = run_length_encoding(sample_input_two)
    print(encoded_result_two)
    sample_input_three = ""
    encoded_result_three = run_length_encoding(sample_input_three)
    print(encoded_result_three)