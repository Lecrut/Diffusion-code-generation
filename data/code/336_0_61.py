import sys
def check_repeated_chars(text: str) -> bool:
    cleaned_text = [char.lower() for char in text if char.isalpha()]
    return len(cleaned_text) != len(set(cleaned_text))
if __name__ == '__main__':
    sample_strings = ["Hello", "Python", "abcdefg"]
    results = []
    for s in sample_strings:
        has_repeat = check_repeated_chars(s)
        status = "Has repeated characters" if has_repeat else "No repeated characters"
        results.append(f"{s}: {status}")
    print("\n".join(results))
    sys.exit(0)