import itertools

def run_length_encode(text: str) -> str:
    if not text:
        return ""
    result = []
    for char, group in itertools.groupby(text):
        count = len(list(group))
        result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbc"
    encoded = run_length_encode(sample_text)
    print(encoded)