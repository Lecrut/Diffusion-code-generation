def encode_string(s):
    if not s:
        return ""
    
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count) + s[i - 1])
            count = 1
    result.append(str(count) + s[-1])
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccd"
    encoded_output = encode_string(sample_input)
    print(encoded_output)