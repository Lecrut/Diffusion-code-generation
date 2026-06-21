def run_length_encode(text: str) -> str:
    if not text:
        return ""
    encoded_parts = [f"{len(list(group))}{char}" for char, group in __import__('itertools').groupby(text)]
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_text = "AAAABBBCCDAA"
    result = run_length_encode(sample_text)
    print(result)