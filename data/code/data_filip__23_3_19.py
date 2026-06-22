import itertools

def run_length_encode(text: str) -> str:
    if not text:
        return ""
    groups = []
    for char, group in itertools.groupby(text):
        count = sum(1 for _ in group)
        groups.append(f"{count}{char}")
    return "".join(groups)

if __name__ == '__main__':
    sample_text = "AAABBBCC"
    encoded = run_length_encode(sample_text)
    print(encoded)