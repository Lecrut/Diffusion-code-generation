def has_repeated_characters(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char not in seen and char.isalpha():                                                                           
            seen.add(char)
        elif char in seen:
            return True
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "The Quick Brown Fox Jumps Over The Lazy Dog"
    ]
    for s in sample_strings:
        result = has_repeated_characters(s)
        print(f"'{s}' contains repeated characters: {result}")