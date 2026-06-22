def run_length_encode(text):
    if not text:
        return ""
    encoded = [(char, len(list(group))) for char, group in __import__('itertools').groupby(text)]
    return "".join(f"{count}{char}" for char, count in encoded)

if __name__ == '__main__':
    sample_text = "aaabbbccccddddde"
    result = run_length_encode(sample_text)
    print(result)