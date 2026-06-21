from itertools import groupby

def run_length_encode(s):
    if not s:
        return ""
    result = []
    for char, group in groupby(s):
        count = len(list(group))
        result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    sample = "AAABBBCCD"
    encoded = run_length_encode(sample)
    print(encoded)

    sample2 = "ABC"
    encoded2 = run_length_encode(sample2)
    print(encoded2)

    sample3 = ""
    encoded3 = run_length_encode(sample3)
    print(encoded3)