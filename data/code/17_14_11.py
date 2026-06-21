def run_length_encoding(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(s[i - 1])
            count = 1
    result.append(str(count))
    result.append(s[-1])
    return "".join(result)

if __name__ == "__main__":
    sample_string = "aaabbcccc"
    encoded_result = run_length_encoding(sample_string)
    print(encoded_result)