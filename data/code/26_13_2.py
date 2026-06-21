def run_length_encode(s):
    if not s:
        return ""

    encoded = []
    count = 1
    current_char = s[0]

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(current_char)
            if count > 1:
                encoded.append(str(count))
            current_char = s[i]
            count = 1

    encoded.append(current_char)
    if count > 1:
        encoded.append(str(count))

    return "".join(encoded)

if __name__ == '__main__':
    sample_strings = ["", "a", "aaa", "aabbbcccc", "aabbccddeeffgghhiijj"]
    for s in sample_strings:
        print(run_length_encode(s))