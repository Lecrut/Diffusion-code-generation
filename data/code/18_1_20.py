def run_length_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    length = len(s)
    for i in range(1, length):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1])
            result.append(str(count))
            count = 1
    result.append(s[-1])
    result.append(str(count))
    return "".join(result)

if __name__ == '__main__':
    input_string = "aaabbc"
    encoded = run_length_encode(input_string)
    print(encoded)