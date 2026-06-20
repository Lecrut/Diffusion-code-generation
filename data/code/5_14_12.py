def capitalize_words(text: str) -> str:
    return text.title()

if __name__ == '__main__':
    samples = [
        "hello world",
        "PYTHON Programming",
        "tHe QuIcK BrOwN fOx",
        "already Capitalized Words",
        "singleword",
        "  spaces   around  "
    ]
    for sample in samples:
        print(capitalize_words(sample))