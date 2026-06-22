import itertools

def run_length_encode(s: str) -> list:
    if not s:
        return []
    groups = itertools.groupby(s)
    encoded = []
    for key, group in groups:
        count = sum(1 for _ in group)
        encoded.append((key, count))
    return encoded

if __name__ == '__main__':
    input_string = "aaabbc"
    result = run_length_encode(input_string)
    print(result)