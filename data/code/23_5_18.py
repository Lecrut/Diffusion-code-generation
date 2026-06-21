def run_length_encode(s):
    if s is None:
        raise TypeError("Input cannot be None")
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if len(s) == 0:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = s[i]
            count = 1
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "aaabbc"
    sample2 = "abc"
    sample3 = "aabbcc"
    sample4 = ""
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    try:
        run_length_encode(None)
    except TypeError as e:
        print(str(e))