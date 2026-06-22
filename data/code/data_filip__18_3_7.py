from itertools import groupby

def run_length_encode(s: str) -> str:
    result = []
    for key, group in groupby(s):
        count = len(list(group))
        result.append(f"{count}{key}")
    return "".join(result)

if __name__ == '__main__':
    sample = "aaabbbbcc"
    encoded = run_length_encode(sample)
    print(encoded)