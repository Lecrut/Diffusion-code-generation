from itertools import groupby

def run_length_encode(data: str) -> tuple[tuple[str, int], ...]:
    return tuple((char, len(list(group))) for char, group in groupby(data))

if __name__ == '__main__':
    sample_data = "aaabbc"
    result = run_length_encode(sample_data)
    print(result)