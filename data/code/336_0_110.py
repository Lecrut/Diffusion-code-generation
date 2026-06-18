def check_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if char not in char_set:
            char_set.add(char)
        else:
            return True
    return False
if __name__ == '__main__':
    sample_string = "Hello World"
    has_repeats = check_repeated_chars(sample_string)
    print(f"String: '{sample_string}'")
    if has_repeats:
        print("Result: Contains repeated characters.")
    else:
        print("Result: No repeated characters found.")