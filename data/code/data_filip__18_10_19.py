from itertools import groupby

def run_length_encode(text: str) -> list[tuple[str, int]]:
    if not text:
        return []
    return [(char, len(list(group))) for char, group in groupby(text)]

if __name__ == '__main__':
    sample = "aaabbbcccaaa"
    result = run_length_encode(sample)
    print(result)