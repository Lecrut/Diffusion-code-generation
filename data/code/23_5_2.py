def run_length_encode(s):
    if s is None:
        raise TypeError("Input must be a string, not None")
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if len(s) == 0:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    sample1 = "AAABBBCCD"
    sample2 = "A"
    sample3 = "ABC"
    sample4 = ""
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    try:
        run_length_encode(None)
    except TypeError:
        print("TypeError raised for None input")