def interleave_strings(str1, str2):
    min_length = min(len(str1), len(str2))
    interleaved = ''.join((a + b for a, b in zip(str1[:min_length], str2[:min_length])))
    interleaved += str1[min_length:] + str2[min_length:]
    return interleaved
if __name__ == '__main__':
    input_str1 = 'abc'
    input_str2 = '12345'
    result = interleave_strings(input_str1, input_str2)
    print(result)