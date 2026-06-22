import itertools

def run_length_encode(s: str) -> list:
    if not s:
        return []
    encoded = []
    for key, group in itertools.groupby(s):
        length = sum(1 for _ in group)
        encoded.append((key, length))
    return encoded

if __name__ == '__main__':
    text = "aabcccccaaa"
    result = run_length_encode(text)
    print(result)