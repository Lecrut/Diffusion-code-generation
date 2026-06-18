def check_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    char_count = {}
    for char in text_lower:
        if not char.isalnum():                                                                                       
            continue
        count = char_count.get(char, 0) + 1
        char_count[char] = count
    return any(count > 1 for count in char_count.values())
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdefg"
    ]
    results = []
    for s in sample_strings:
        has_repeat = check_repeated_chars(s)
        status = "Has repeated characters" if has_repeat else "No repeated characters"
        results.append(f"'{s}': {status}")
    print("\n".join(results))