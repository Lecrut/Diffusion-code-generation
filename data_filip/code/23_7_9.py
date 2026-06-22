def compress_string(input_str):
    if not input_str:
        return ""
    
    segments = []
    active_char = input_str[0]
    run_length = 1
    
    for index in range(1, len(input_str)):
        if input_str[index] == active_char:
            run_length += 1
        else:
            segments.append(str(run_length) + active_char)
            active_char = input_str[index]
            run_length = 1
            
    segments.append(str(run_length) + active_char)
    return "".join(segments)

if __name__ == '__main__':
    test_case_1 = "aaabbcd"
    print(compress_string(test_case_1))
    test_case_2 = "a"
    print(compress_string(test_case_2))
    test_case_3 = ""
    print(compress_string(test_case_3))
    test_case_4 = "AABBBCC"
    print(compress_string(test_case_4))