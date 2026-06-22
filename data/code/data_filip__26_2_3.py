def run_length_encode(s):
    if not s:
        return []
    encoded_pairs = []
    current_char = s[0]
    run_length = 1
    for char in s[1:]:
        if char == current_char:
            run_length += 1
        else:
            encoded_pairs.append((current_char, run_length))
            current_char = char
            run_length = 1
    encoded_pairs.append((current_char, run_length))
    return encoded_pairs

if __name__ == '__main__':
    test_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
    result = run_length_encode(test_string)
    print(result)
    empty_result = run_length_encode("")
    print(empty_result)
    single_result = run_length_encode("Z")
    print(single_result)