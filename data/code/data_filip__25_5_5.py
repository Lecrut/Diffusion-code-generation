from itertools import groupby

def run_length_encode(data: str) -> list[tuple[str, int]]:
    return [(char, len(list(group))) for char, group in groupby(data)]

if __name__ == '__main__':
    sample = "AAABBBCCD"
    result = run_length_encode(sample)
    print(result)