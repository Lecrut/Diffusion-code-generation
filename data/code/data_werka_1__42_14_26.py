def interleave_strings(str1: str, str2: str) -> str:
    result = []
    len1, len2 = (len(str1), len(str2))
    max_length = max(len1, len2)
    for i in range(max_length):
        if i < len1:
            result.append(str1[i])
        if i < len2:
            result.append(str2[i])
    return ''.join(result)
if __name__ == '__main__':
    sample_str1 = 'abc'
    sample_str2 = '12345'
    interleaved_result = interleave_strings(sample_str1, sample_str2)
    print(interleaved_result)