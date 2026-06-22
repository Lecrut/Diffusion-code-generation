def run_length_encode(s):
    if s is None:
        raise TypeError("Input cannot be None")
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if len(s) == 0:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == '__main__':
    print(run_length_encode("aaabbbcc"))
    print(run_length_encode("abc"))
    print(run_length_encode(""))
    print(run_length_encode("aaaaa"))
    try:
        run_length_encode(None)
    except TypeError as e:
        print(e)