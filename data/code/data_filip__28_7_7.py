import itertools

def rle_encode(text: str) -> str:
    if not text:
        return ""

    def generator():
        for char, group in itertools.groupby(text):
            count = len(list(group))
            yield f"{count}{char}"

    return "".join(generator())

if __name__ == '__main__':
    sample_text = "aabcccccaaa"
    result = rle_encode(sample_text)
    print(result)