import itertools

def run_length_encode(text: str) -> str:
    if not text:
        return ""
    encoded_parts = []
    for char, group in itertools.groupby(text):
        length = len(list(group))
        encoded_parts.append(f"{length}{char}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_text = "aabcccccaaa"
    result = run_length_encode(sample_text)
    print(result)