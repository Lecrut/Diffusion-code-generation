def interleave_strings(str1, str2):
    interleaved = []
    len_str1, len_str2 = (len(str1), len(str2))
    max_len = max(len_str1, len_str2)
    for i in range(max_len):
        if i < len_str1:
            interleaved.append(str1[i])
        if i < len_str2:
            interleaved.append(str2[i])
    return ''.join(interleaved)
if __name__ == '__main__':
    sample_str1 = 'abc'
    sample_str2 = '12345'
    result = interleave_strings(sample_str1, sample_str2)
    print(result)