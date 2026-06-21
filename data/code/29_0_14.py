def run_length_encode(input_string):
    if not input_string:
        return ""
    result = []
    count = 1
    length = len(input_string)
    for i in range(1, length):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            result.append(str(count) + input_string[i - 1])
            count = 1
    result.append(str(count) + input_string[length - 1])
    return "".join(result)

if __name__ == '__main__':
    test_cases = [
        "aaabbccccd",
        "aaaaaaaaaa",
        "a",
        "",
        "abcde"
    ]
    for text in test_cases:
        encoded = run_length_encode(text)
        print(encoded)