def check_repeated_characters(text: str) -> bool:
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return len(cleaned_text) != len(set(cleaned_text))
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "abcdefg",
        "Programming is fun!",
        "The quick brown fox jumps over the lazy dog"
    ]
    for s in sample_strings:
        result = check_repeated_characters(s)
        status = "Contains repeated characters" if result else "No repeated characters found"
        print(f"'{s}': {status}")