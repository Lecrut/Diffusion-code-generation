def has_repeated_characters(text):
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
    result = has_repeated_characters(sample_string)
    print(f"Input string: {sample_string}")
    if result:
        print("Result: Repeated characters found.")
    else:
        print("Result: No repeated characters found.")