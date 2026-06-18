def contains_repeated_characters(s):
    s_lower = s.lower()
    seen_chars = set()
    for char in s_lower:
        if char in seen_chars:
            return True, f"Repeated character found: '{char}'"
        seen_chars.add(char)
    return False, "No repeated characters found."
if __name__ == '__main__':
    sample_strings = [
        ("Hello World",),
        ("abcdefg",),
        ("The Quick Brown Fox Jumped Over The Lazy Dog",),
        ("Python Programming 101",)
    ]
    for s in sample_strings:
        has_repeat, message = contains_repeated_characters(s[0])
        print(f"Input: '{s[0]}'")
        if has_repeat:
            print(message)
        else:
            print("No repetition detected.")