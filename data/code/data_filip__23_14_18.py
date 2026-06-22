def run_length_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count) + s[i - 1])
            count = 1
    result.append(str(count) + s[-1])
    return "".join(result)

if __name__ == '__main__':
    sample_input_1 = "aaabbcccc"
    sample_input_2 = "a"
    sample_input_3 = ""
    sample_input_4 = "ab"
    print(run_length_encode(sample_input_1))
    print(run_length_encode(sample_input_2))
    print(run_length_encode(sample_input_3))
    print(run_length_encode(sample_input_4))