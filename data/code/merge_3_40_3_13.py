def extract_first_letters(s: str) -> str:
    return ' '.join(word[0] if word else '' for word in s.split())

if __name__ == '__main__':
    samples = ["hello world", "  python coding ", "", "single"]
    print("Input:", repr(samples))
    print("Output:")
    for inp in samples:
        print(f"  {repr(inp)} -> {extract_first_letters(inp)}")