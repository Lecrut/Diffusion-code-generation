def interleave_strings(str1, str2):
    result = []
    len_str1, len_str2 = len(str1), len(str2)
    max_len = max(len_str1, len_str2)
    
    for i in range(max_len):
        if i < len_str1:
            result.append(str1[i])
        if i < len_str2:
            result.append(str2[i])
    
    return ''.join(result)

if __name__ == '__main__':
    sample_input1 = "abc"
    sample_input2 = "12345"
    interleaved_string = interleave_strings(sample_input1, sample_input2)
    print(interleaved_string)