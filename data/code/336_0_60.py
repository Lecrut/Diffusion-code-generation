def check_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if char not in char_set and (char.isalpha()):
            char_set.add(char)
    return len(set(c for c in text_lower)) != len(text_lower.replace(' ', '').replace('\n', ''))
def main():
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdef"
    ]
    results = []
    for s in sample_strings:
        has_repeat = check_repeated_chars(s)
        status = "Has repeated characters" if has_repeat else "No repeated characters"
        results.append(f"'{s}': {status}")
    print("\n".join(results))
if __name__ == '__main__':
    main()