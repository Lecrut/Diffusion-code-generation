def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(s[i - 1] + str(count))
            count = 1
    encoded.append(s[-1] + str(count))
    return "".join(encoded)

if __name__ == '__main__':
    test_string = "aaabbbccdddd"
    result = run_length_encode(test_string)
    print(result)