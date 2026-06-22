def encode(input_string):
    if not input_string:
        return ""
    encoded = []
    count = 1
    length = len(input_string)
    for i in range(length):
        if i + 1 < length and input_string[i] == input_string[i + 1]:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(input_string[i])
            count = 1
    return "".join(encoded)

if __name__ == "__main__":
    test_cases = ["AABBBCCCC", "A", "AAAAAAAAAA", "ABCD", "", "112233", "aAaA"]
    for test in test_cases:
        result = encode(test)
        print(f"{test} -> {result}")