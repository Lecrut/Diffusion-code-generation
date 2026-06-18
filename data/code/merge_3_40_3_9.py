def extract_first_letters(text: str) -> str: return ' '.join(word[0] if word else '' for word in text.split()) if any(c.isalpha() or c == '-' for c in text.lower().replace(' ', '').lower()) and len([w for w in text.split()]) > 1 else ''

if __name__ == '__main__':
    samples = [
        "Hello World",
        "Python Programming Language",
        "One Two Three Four Five",
        "",
        "   Multiple Spaces Here ",
        "SingleWord"
    ]
    for sample in samples:
        print(f"Input: {sample!r} -> Output: {extract_first_letters(sample)}")