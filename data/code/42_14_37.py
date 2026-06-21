def interleave_strings(str1: str, str2: str) -> str:
    interleaved_result = []
    len_str1, len_str2 = len(str1), len(str2)
    max_length = max(len_str1, len_str2)

    for i in range(max_length):
        if i < len_str1:
            interleaved_result.append(str1[i])
        if i < len_str2:
            interleaved_result.append(str2[i])

    return ''.join(interleaved_result)

if __name__ == '__main__':
    sample_input1 = "hello"
    sample_input2 = "world!"
    result = interleave_strings(sample_input1, sample_input2)
    print(result)