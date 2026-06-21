from itertools import groupby

def run_length_encode(s):
    if not s:
        return []
    encoded = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        encoded.append((char, count))
    return encoded

if __name__ == '__main__':
    sample = "aaabbcdddd"
    result = run_length_encode(sample)
    print(result)