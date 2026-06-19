def interleave_strings(str1: str, str2: str) -> str:
    result = []
    len1, len2 = (len(str1), len(str2))
    max_len = max(len1, len2)
    for i in range(max_len):
        if i < len1:
            result.append(str1[i])
        if i < len2:
            result.append(str2[i])
    return ''.join(result)
if __name__ == '__main__':
    str1 = 'abc'
    str2 = '12345'
    interleaved = interleave_strings(str1, str2)
    print(interleaved)