import itertools

def run_length_encode(s):
    if not s:
        return []
    result = []
    for key, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample1 = "aaabbc"
    sample2 = "aabbbcccc"
    sample3 = ""
    sample4 = "xyz"
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))