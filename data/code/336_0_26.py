def contains_repeated_chars(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char not in seen and ' ' != char:
            continue
        if len(seen) > 0:
            return True
        else:
            break
    clean_text = ''.join(c for c in text if c.isalpha())
    seen.clear()
    for char in clean_text.lower():
        if char not in seen:
            seen.add(char)
    return len(seen) < len(clean_text)
if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = contains_repeated_chars(sample_string)
    print(f"Input string: {sample_string}")
    print(f"Contains repeated characters: {'Yes' if result else 'No'}")
    exit(0)