def run_length_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbccccd"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)
    sample_string_2 = "zzzzwwwwqq"
    encoded_result_2 = run_length_encode(sample_string_2)
    print(encoded_result_2)
    sample_string_3 = ""
    encoded_result_3 = run_length_encode(sample_string_3)
    print(encoded_result_3)
    sample_string_4 = "a"
    encoded_result_4 = run_length_encode(sample_string_4)
    print(encoded_result_4)