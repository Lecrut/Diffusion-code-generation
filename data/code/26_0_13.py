import itertools

def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    for key, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        encoded.append(f"{count}{key}")
    return "".join(encoded)

if __name__ == '__main__':
    sample1 = "AAABBBCCD"
    sample2 = "ABCD"
    sample3 = "AAAAAA"
    sample4 = ""
    sample5 = "AABBCC"
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))