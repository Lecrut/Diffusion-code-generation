import itertools

def run_length_encode(text: str) -> list:
    if not text:
        return []
    encoded = []
    for char, group in itertools.groupby(text):
        count = sum((1 for _ in group))
        encoded.append((char, count))
    return encoded
if __name__ == '__main__':
    sample_string = 'aaabbc'
    result = run_length_encode(sample_string)
    print(result)