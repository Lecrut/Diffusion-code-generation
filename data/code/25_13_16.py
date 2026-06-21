import itertools
import sys

def run_length_encode(s):
    if not s:
        return ""
    result = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{count}{char}")
    return "".join(result)

def run_length_decode(s):
    if not s:
        return ""
    result = []
    i = 0
    length = len(s)
    while i < length:
        count_str = []
        while i < length and s[i].isdigit():
            count_str.append(s[i])
            i += 1
        if not count_str:
            raise ValueError("Invalid encoding: missing count")
        count = int("".join(count_str))
        if i >= length:
            raise ValueError("Invalid encoding: missing character")
        char = s[i]
        result.append(char * count)
        i += 1
    return "".join(result)

if __name__ == '__main__':
    input_string = "AAAAABBBCCD"
    encoded = run_length_encode(input_string)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)