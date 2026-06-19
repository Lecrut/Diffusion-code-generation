def interleave_strings(str1: str, str2: str) -> str:
    result = []
    len_str1 = len(str1)
    len_str2 = len(str2)
    max_length = max(len_str1, len_str2)

    for i in range(max_length):
        if i < len_str1:
            result.append(str1[i])
        if i < len_str2:
            result.append(str2[i])

    return ''.join(result)

if __name__ == '__main__':
    SAMPLE_INPUT_1 = "abc"
    SAMPLE_INPUT_2 = "12345"
    interleaved_result = interleave_strings(SAMPLE_INPUT_1, SAMPLE_INPUT_2)
    print(interleaved_result)