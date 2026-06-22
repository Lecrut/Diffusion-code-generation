import itertools

def rle_encode(text: str) -> str:
    if not text:
        return ""
    return "".join(f"{count}{char}" for char, count in [(c, len(list(g))) for c, g in itertools.groupby(text)])

if __name__ == '__main__':
    sample_text = "aaaabccc"
    result = rle_encode(sample_text)
    print(result)