from itertools import groupby

def run_length_encode(s):
    if not s:
        return []
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        result.append((char, count))
    return result

if __name__ == '__main__':
    sample_strings = [
        "AAABBBCCDAA",
        "A",
        "ABABAB",
        "",
        "AAAAA"
    ]
    for s in sample_strings:
        encoded = run_length_encode(s)
        print(encoded)