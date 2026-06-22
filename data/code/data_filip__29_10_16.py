def encode_consecutive(s):
    if not s:
        return ""
    encoded_chars = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded_chars.append(current_char)
            encoded_chars.append(str(count))
            current_char = s[i]
            count = 1
    encoded_chars.append(current_char)
    encoded_chars.append(str(count))
    return "".join(encoded_chars)

if __name__ == '__main__':
    sample_string = "aaabbc"
    result = encode_consecutive(sample_string)
    print(result)