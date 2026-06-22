import itertools

def run_length_encode(text: str) -> list:
    result = []
    if not text:
        return result
    for key, group in itertools.groupby(text):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample_text = "aaabbc"
    encoded = run_length_encode(sample_text)
    print(encoded)