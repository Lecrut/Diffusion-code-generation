def normalize_text(text):
    normalized = text.strip()
    return frozenset((normalized,))

def main():
    sample_texts = [
        "  hello world  ",
        "  python  programming  ",
        "  leading spaces  ",
        "trailing spaces  ",
        "  both  ",
        "no spaces",
        "   ",
        ""
    ]
    for sample in sample_texts:
        result = normalize_text(sample)
        print(result)

if __name__ == '__main__':
    main()