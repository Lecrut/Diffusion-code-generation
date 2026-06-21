from itertools import groupby

def compress_identical_chars(s):
    if not s:
        return ""
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        if count > 1:
            result.append(f"{count}{char}")
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    test_string = "aaabbcddde"
    print(compress_identical_chars(test_string))