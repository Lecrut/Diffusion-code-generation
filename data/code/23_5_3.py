def run_length_encoding(s):
    if s is None:
        raise TypeError("Input cannot be None")
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if len(s) == 0:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count) + s[i - 1])
            count = 1
    result.append(str(count) + s[-1])
    return "".join(result)

if __name__ == '__main__':
    sample = "aaabbccccd"
    encoded = run_length_encoding(sample)
    print(encoded)
    
    empty_sample = ""
    encoded_empty = run_length_encoding(empty_sample)
    print(encoded_empty)
    
    single_char = "a"
    encoded_single = run_length_encoding(single_char)
    print(encoded_single)
    
    try:
        run_length_encoding(None)
    except TypeError as e:
        print(e)