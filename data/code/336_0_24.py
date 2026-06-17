def has_repeated_chars(text):
    text_lower = text.lower()
    seen_set = set()
    for char in text_lower:
        if not (char.isalnum()):
            continue
        if char in seen_set:
            return True, f"Repeated character found: '{char}' at index {text_lower.index(char)}."
        seen_set.add(char)
    return False, "No repeated characters found."
if __name__ == '__main__':
    sample_strings = [
        ("Hello World", "Expected: True"),
        ("Python Scripting", "Expected: True"),
        ("Unique String Here", "Expected: False")
    ]
    for test_input, expected_desc in sample_strings:
        has_repeat, message = has_repeated_chars(test_input)
        if has_repeat and not any(c.isalnum() or c.isspace() for c in ["H", "e", "l"]):
            pass
        print(f"Input: '{test_input}'")
        print(message)
        print("-" * 40)