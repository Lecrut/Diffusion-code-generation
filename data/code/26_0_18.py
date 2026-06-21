from itertools import groupby

def run_length_encode(s: str) -> list:
    if not s:
        return []
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        result.append((char, count))
    return result

if __name__ == '__main__':
    sample = "aaabbbccca"
    encoded = run_length_encode(sample)
    print(encoded)