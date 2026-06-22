def run_length_encoding(s):
    if not s:
        return ""
    result = []
    count = 1
    length = len(s)
    for i in range(length):
        if i + 1 < length and s[i] == s[i + 1]:
            count += 1
        else:
            result.append(f"{count}{s[i]}")
            count = 1
    return "".join(result)

if __name__ == "__main__":
    test_string = "aaabbccccdddeee"
    encoded_value = run_length_encoding(test_string)
    print(encoded_value)