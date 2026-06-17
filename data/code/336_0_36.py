def check_repeated_characters(text: str) -> bool:
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())
    return len(cleaned_text) != len(set(cleaned_text))
if __name__ == '__main__':
    sample_strings = ["hello", "world", "abcdef"]
    has_repeated_found = False
    for s in sample_strings:
        result = check_repeated_characters(s)
        if result:
            print(f"'{s}' contains repeated characters.")
            has_repeated_found = True
        else:
            print(f"'{s}' does not contain repeated characters.")
    exit(0)