from itertools import groupby

def run_length_encode(text: str) -> list:
    return [(char, sum(1 for _ in group)) for char, group in groupby(text)]

if __name__ == '__main__':
    result = run_length_encode("aaabbcccc")
    print(result)