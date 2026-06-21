def interleave_strings(str1: str, str2: str) -> str:
    INTERLEAVE_LIMIT = 1000
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError('Both inputs must be strings.')
    len_str1, len_str2 = (len(str1), len(str2))
    max_len = min(max(len_str1, len_str2), INTERLEAVE_LIMIT)
    interleaved_chars = []
    for i in range(max_len):
        if i < len_str1:
            interleaved_chars.append(str1[i])
        if i < len_str2:
            interleaved_chars.append(str2[i])
    return ''.join(interleaved_chars)
if __name__ == '__main__':
    SAMPLE_INPUT_1 = 'hello'
    SAMPLE_INPUT_2 = 'world!'
    interleaved_string = interleave_strings(SAMPLE_INPUT_1, SAMPLE_INPUT_2)
    print(interleaved_string)