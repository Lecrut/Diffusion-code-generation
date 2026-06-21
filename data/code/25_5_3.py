import itertools

def run_length_encode(s: str) -> list:
    result = []
    for key, group in itertools.groupby(s):
        count = len(list(group))
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample = "aaabbcc"
    encoded = run_length_encode(sample)
    print(encoded)