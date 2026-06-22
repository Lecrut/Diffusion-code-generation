def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            encoded.append(str(count) + s[i-1])
            count = 1
    encoded.append(str(count) + s[-1])
    return "".join(encoded)

def run_length_decode(s):
    if not s:
        return ""
    decoded = []
    i = 0
    while i < len(s):
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        count = int(num_str)
        char = s[i]
        decoded.append(char * count)
        i += 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_input = "AAAABBBCCDAA"
    encoded = run_length_encode(sample_input)
    decoded = run_length_decode(encoded)
    print(sample_input == decoded)