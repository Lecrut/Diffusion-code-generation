import itertools
import sys

def run_length_encode(s: str) -> list:
    if not s:
        return []
    encoded = []
    for key, group in itertools.groupby(s):
        count = len(list(group))
        encoded.append((key, count))
    return encoded

if __name__ == '__main__':
    text = "aaabbc"
    result = run_length_encode(text)
    print(result)