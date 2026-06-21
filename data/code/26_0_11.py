from itertools import groupby

def run_length_encode(s):
    result = []
    for key, group in groupby(s):
        count = sum(1 for _ in group)
        result.append((count, key))
    return result

if __name__ == '__main__':
    sample_input = "AAABBBCCD"
    encoded = run_length_encode(sample_input)
    print(encoded)