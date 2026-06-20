def get_repeated_chars(text: str) -> str:
    seen = set()
    duplicates = set()
    for char in text:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return ''.join(sorted(duplicates))

if __name__ == '__main__':
    sample_text = "programming"
    result = get_repeated_chars(sample_text)
    print(result)