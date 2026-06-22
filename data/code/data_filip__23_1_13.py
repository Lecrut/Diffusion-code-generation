import itertools

def run_length_encode(s):
    if not s:
        return ""
    result = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        result.append(f"{count}{char}")
    return "".join(result)

def run_length_decode(s):
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        if not s[i].isdigit():
            result.append(s[i])
            i += 1
        else:
            count_start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            count = int(s[count_start:i])
            char = s[i]
            result.append(char * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    encoded = run_length_encode(sample_string)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)