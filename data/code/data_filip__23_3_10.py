import itertools

def run_length_encode(text):
    if not text:
        return ""
    result = []
    for char, group in itertools.groupby(text):
        count = sum(1 for _ in group)
        result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbcddd"
    encoded = run_length_encode(sample_text)
    print(encoded)