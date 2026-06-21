def run_length_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{count}{s[i - 1]}")
            count = 1
    result.append(f"{count}{s[-1]}")
    return "".join(result)

def run_length_decode(s):
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        count = 0
        while i < len(s) and s[i].isdigit():
            count = count * 10 + int(s[i])
            i += 1
        if i < len(s):
            char = s[i]
            result.append(char * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    original_string = "AAAAAAAAAABBBBBCCCC"
    encoded = run_length_encode(original_string)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
    print(original_string == decoded)