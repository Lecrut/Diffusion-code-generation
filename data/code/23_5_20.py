def compress_string(s):
    if s is None:
        raise TypeError("Input cannot be None")
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if s == "":
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = s[i]
            count = 1
    encoded.append(current_char + str(count))
    return "".join(encoded)

if __name__ == "__main__":
    test_cases = [
        "aaabbcccc",
        "a",
        "",
        "aAaA",
        "112233",
        "aa a a"
    ]
    for test in test_cases:
        result = compress_string(test)
        print(f"Input: {repr(test)} -> Output: {result}")
    try:
        compress_string(None)
    except TypeError as e:
        print(f"Input: None -> Error: {e}")