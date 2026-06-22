import itertools

def run_length_encode(text: str) -> list:
    if not text:
        return []
    encoded = []
    for key, group in itertools.groupby(text):
        count = sum(1 for _ in group)
        encoded.append((key, count))
    return encoded

if __name__ == '__main__':
    result = run_length_encode("aaabbc")
    print(result)